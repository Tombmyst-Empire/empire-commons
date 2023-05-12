from rapidfuzz import fuzz_cpp
from statistics import fmean, mean as py_mean
from empire_commons.types_ import NULL as ENULL
import re
import random
import math

cdef REGROUP_NUMBER_REGEX = re.compile(r"([\d]*[.]?[\d]+)")


cdef class Vec2D:
    def __cinit__(self, double x, double y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vec2D(%f, %f)" % (self.x, self.y)

    cdef inline bint is_nan(self):
        return self.x == self.y == math.nan

# ==================================================================================== MATH UTIL

cpdef double math_util_avg(tuple data):
    with nogil:
        if not data:
            return 0.0

    try:
        return fmean(data)
    except:
        return py_mean(data)


cpdef int math_util_clamp_int(int number, int minimum, int maximum):
    if number < minimum:
        return minimum
    elif number > maximum:
        return maximum
    else:
        return number


cpdef float math_util_clamp_float(double number, double minimum, double maximum):
    if number < minimum:
        return minimum
    elif number > maximum:
        return maximum
    else:
        return number

# ========================================================================================================================== DICT UTIL

cpdef dict dict_util_swap_key_values(dict the_dict):
    """
    Swap a dictionary keys and values
    """
    return {value: key for key, value in the_dict.items()}


cpdef dict dict_util_remap(dict the_dict, dict mapping):
    """
    Remaps the given directory using the provided mapping.

    The mapping keys represent the provided dictionary keys and mapping values represent
    the desired keys.
    """
    return {
        mapping.get(key, key): value
        for key, value in the_dict.items()
    }


cpdef dict_util_get_first_non_null(dict the_dict, tuple fields, default = None):
    """
    Returns the first non-None value from a sequence of fields of a dictionary.
    If none of the fields returned a non-None value, then the method return *default*.

    """
    for field in fields:
        if the_dict.get(field):
            return the_dict[field]
    return default


cpdef dict dict_util_try_del(dict the_dict, object key):
    """
    Tries to delete a fields from a dictionary.
    """
    if key in the_dict:
        del the_dict[key]

# ========================================================================================================================== FUZZ UTIL

cpdef str fuzz_util_get_highest_scoring_string(
        str item,
        tuple candidates,
        object method = fuzz_cpp.token_sort_ratio
):
    cdef float highest_score = 0.0
    cdef str highest_candidate = None
    cdef float ratio = 0.0

    for candidate in candidates:
        ratio = method(item, candidate)
        if ratio > highest_score:
            highest_score = ratio
            highest_candidate = candidate

    return highest_candidate


cpdef double fuzz_util_get_fuzz_average(
        str lhs,
        str rhs,
        tuple methods
):
    methods = methods or (fuzz_cpp.token_sort_ratio, fuzz_cpp.ratio, fuzz_cpp.token_set_ratio)
    return math_util_avg(tuple([method(lhs, rhs) for method in methods]))

# ========================================================================================================================== LIST DICT UTIL

cpdef list list_dict_util_keep_root_keys(list the_list, tuple keys):
    return [
        {
            a_dict_key: a_dict_value
            for a_dict_key, a_dict_value in a_dict.items()
            if a_dict_key in keys
        }
        for a_dict in the_list
    ]

cpdef dict list_dict_util_create_dict_from_list_of_dicts(list the_list, str key):
    return {item[key]: item for item in the_list}


cpdef dict list_dict_util_create_dict_from_list_of_objects(list the_list, str key):
    return {getattr(item, key): item for item in the_list}


cpdef bint list_dict_util_exists_within_a_list_of_dicts(
        list the_list,
        object key_to_match,
        object value_to_match = ENULL
):
    for item in the_list:
        if key_to_match in item and (
            value_to_match is ENULL or item[key_to_match] == value_to_match
        ):
            return True
    return False


cpdef dict list_dict_util_get_within_a_list_of_dicts(
        list the_list,
        object dictionary_key,
        object dictionary_value = ENULL,
        object default_value = ENULL
):
    for item in the_list:
        if (dictionary_key in item and dictionary_value == ENULL) or item.get(
                dictionary_key
        ) == dictionary_value:
            return item

    return default_value or {}

# ========================================================================================================================== LIST UTIL

cdef inline void _list_util_maybe_add(
        set processed,
        object method,
        str list_element,
        str to_be_found,
        bint ignore_case
):
    if (
            (
                ignore_case and
                method(list_element.lower(), to_be_found.lower())
            ) or
        method(list_element, to_be_found)
    ):
        processed.add(list_element)


cdef inline void _list_util_apply_filters(
        list the_list,
        set processed,
        tuple using,
        object method,
        bint ignore_case
):
    if using:
        for to_be_found in using:
            [
                _list_util_maybe_add(processed, method, list_element, to_be_found, ignore_case)
                for list_element in the_list
            ]


cpdef object list_util_try_get(list the_list, unsigned int index, object default_value = None):
    if 0 <= index < len(the_list):
        return the_list[index]

    return default_value


cpdef bint list_util_contains_sub_list(list lhs, list rhs):
    cdef list longest
    cdef list sub_list

    if len(lhs) > len(rhs):
        longest = lhs
        sub_list = rhs
    else:
        longest = rhs
        sub_list = lhs

    return set(sub_list).issubset(set(longest))


cpdef list list_util_filter_list_of_strings(
        list the_list,
        tuple must_start_with = None,
        tuple must_end_with = None,
        tuple must_contain = None,
        bint ignore_case = False
):
    if not the_list:
        return the_list

    cdef set processed = set()

    _list_util_apply_filters(the_list, processed, must_start_with, str.startswith, ignore_case)
    _list_util_apply_filters(the_list, processed, must_end_with, str.endswith, ignore_case)
    _list_util_apply_filters(the_list, processed, must_contain, str.__contains__, ignore_case)

    return list(processed)


cpdef bint list_util_equals(list lhs, list rhs, bint ignore_order = True):
    if ignore_order:
        if len(lhs) != len(rhs):
            return False

        if (
                len(lhs) < 37
        ):  # number established with benchmarks. The following gets slower when list is longer than 37
            # TODO: should be revalidated in Cython as this was performed in Python
            for item in lhs:
                if item not in rhs:
                    return False
            return True

        return set(lhs) == set(rhs)  # TODO: ça va supprimer tous les dupes ça!

    return lhs == rhs


cpdef list list_util_expand_right(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    return list_util_expand_right_inplace(list(the_list), expansion_size, filler)


cpdef list list_util_expand_right_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    if callable(filler):
        the_list.extend([filler(i) for i in range(expansion_size)])
    else:
        the_list.extend([filler for i in range(expansion_size)])
    return the_list


cpdef list list_util_expand_left(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    return list_util_expand_left_inplace(list(the_list), expansion_size, filler)


cpdef list list_util_expand_left_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    if callable(filler):
        for i in range(expansion_size):
            the_list.insert(i, filler(i))
    else:
        for _ in range(expansion_size):
            the_list.insert(0, filler)

    return the_list


cpdef list list_util_generate_random_list_of_ints(
        unsigned int length,
        int min_bound = 0,
        int max_bound = 1_000_000
):
    return [random.randint(min_bound, max_bound) for _ in range(length)]


cpdef list list_util_rotate_left(
        list the_list,
        unsigned int rotation_size
):
    return the_list[rotation_size:] + the_list[:rotation_size]


cpdef list list_util_rotate_right(
        list the_list,
        unsigned int rotation_size
):
    return the_list[-rotation_size:] + the_list[:-rotation_size]


cpdef list list_util_chunk_list(
        list the_list,
        unsigned int chunk_size
):
    return [the_list[i:i + chunk_size] for i in range(0, len(the_list), chunk_size)]


cpdef void list_util_append_if(list the_list, bint condition, object value):
    if condition:
        the_list.append(value)

# ========================================================================================================================== NUMBER UTIL

cpdef int number_util_to_int(str s, int default = 0, bint strip_non_numeric_chars = False):
    if strip_non_numeric_chars:
        s = "".join(REGROUP_NUMBER_REGEX.findall(s))

    try:
        return int(s)
    except:
        return default

# ========================================================================================================================== SET UTIL

cpdef bint set_util_contains_sub_set(set lhs, set rhs):
    cdef set longest
    cdef set sub_list

    if len(lhs) > len(rhs):
        longest = lhs
        sub_list = rhs
    else:
        longest = rhs
        sub_list = lhs

    return sub_list.issubset(longest)

# ========================================================================================================================== SLICE UTIL

cpdef bint slice_util_number_is_in(
        slice slice_obj,
        int number,
        bint inclusive = False
):
    if slice_obj is None:
        return False

    cdef slice_copy

    if slice_obj.start < 0:
        slice_copy = slice(None, slice_obj.stop)
    elif slice_obj.stop < 0:
        slice_copy = slice(slice_obj.start, None)
    else:
        slice_copy = slice_obj

    if None not in [slice_copy.start, slice_copy.stop]:
        if inclusive:
            return slice_copy.start <= number <= slice_copy.stop
        else:
            return slice_copy.start <= number < slice_copy.stop
    elif slice_copy.start is slice_copy.stop is None:
        return True
    elif slice_copy.start is None:
        if inclusive:
            return number <= slice_copy.stop
        else:
            return number < slice_copy.stop
    elif slice_copy.stop is None:
        return slice_copy.start <= number

    return False


cpdef bint slice_util_contains(
        slice containing_slice,
        slice slice_to_be_contained
):
    return (
        slice_to_be_contained.start >= containing_slice.start and
        slice_to_be_contained.stop < containing_slice.stop
    )


cpdef slice slice_util_get_slice_with_most_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
):
    cdef Vec2D coverage = slice_util_get_slice_coverage(reference_slice, slice_a, slice_b)

    if coverage.is_nan():
        return None
    elif coverage.y == math.nan or coverage.x >= coverage.y:
        return slice_a

    return slice_b


cpdef Vec2D slice_util_get_slice_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
):
    cdef int value_a = slice_a.stop
    cdef int value_b = slice_b.start
    cdef int distance_a
    cdef int distance_b
    cdef int total_distance


    if value_a is value_b is None:
        return Vec2D(math.nan, math.nan)
    elif value_a is None or reference_slice.start is None:
        return Vec2D(100.0, 0.0)
    elif value_b is None:
        return Vec2D(0.0, 100.0)
    else:
        distance_a = abs(abs(value_a) - reference_slice.start)
        distance_b = abs(abs(value_b) - (reference_slice.stop or 0))
        total_distance = distance_a + distance_b
        return Vec2D(
            distance_a * 100 / total_distance,
            distance_b * 100 / total_distance
        )

# ========================================================================================================================== STRING CASING

cpdef str string_casing_to_camel_case_strip_spaces(str the_string):
    cdef camel_case = string_casing_to_pascal_case_strip_spaces(the_string)
    return camel_case[0].lower() + camel_case[1:]

cpdef str string_casing_to_camel_case_with_underscores(str the_string):
    cdef camel_case = string_casing_to_pascal_case_with_underscores(the_string)
    return camel_case[0].lower() + camel_case[1:]

cpdef str string_casing_to_pascal_case_strip_spaces(str the_string):
    if not the_string:
        return the_string

    cdef words = (the_string
                  .replace(' ', ' ')
                  .replace('-', ' ')
                  .replace('.', ' ')
                  .replace(',', ' ')
                  .replace(':', ' ')
                  .replace(';', ' ')).split()

    cdef result = []
    for word in words:
        result.append(word.capitalize())

    cdef joint_result = ''.join(result)
    return joint_result

cpdef str string_casing_to_pascal_case_with_underscores(str the_string):
    if not the_string:
        return the_string

    cdef words = (the_string
                  .replace(' ', ' ')
                  .replace('-', ' ')
                  .replace('.', ' ')
                  .replace(',', ' ')
                  .replace(':', ' ')
                  .replace(';', ' ')).split()

    cdef result = []
    for word in words:
        result.append(word.capitalize())

    cdef joint_result = '_'.join(result)
    return joint_result

cpdef str string_casing_to_upper_case_with_underscores(str the_string):
    if not the_string:
        return the_string

    return the_string.upper()\
        .replace(' ', '_')\
        .replace('-', '_')\
        .replace('.', '_')\
        .replace(',', '_')\
        .replace(':', '_')\
        .replace(';', '_')

# ========================================================================================================================== TUPLE UTIL

cpdef object tuple_util_try_get(tuple the_tuple, unsigned int index, object default_value = None):
    if 0 <= index < len(the_tuple):
        return the_tuple[index]

    return default_value


cpdef bint tuple_util_tuple_contains_sub_tuple(tuple lhs, tuple rhs):
    cdef tuple longest
    cdef tuple sub_list

    if len(lhs) > len(rhs):
        longest = lhs
        sub_list = rhs
    else:
        longest = rhs
        sub_list = lhs

    return set(sub_list).issubset(set(longest))

