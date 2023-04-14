import random

from empire.commons.types_ import _NULL

cpdef object try_get(list the_list, unsigned int index, object default_value = None):
    if 0 <= index < len(the_list):
        return the_list[index]
    else:
        return default_value


cpdef bint list_contains_sub_list(list lhs, list rhs):
    cdef list longest
    cdef list sub_list

    if len(lhs) > len(rhs):
        longest = lhs
        sub_list = rhs
    else:
        longest = rhs
        sub_list = lhs

    return set(sub_list).issubset(set(longest))


cpdef bint set_contains_sub_list(set lhs, set rhs):
    cdef set longest
    cdef set sub_list

    if len(lhs) > len(rhs):
        longest = lhs
        sub_list = rhs
    else:
        longest = rhs
        sub_list = lhs

    return sub_list.issubset(longest)


cdef inline void _maybe_add(
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


cdef inline void _apply_filters(
        list the_list,
        set processed,
        tuple using,
        object method,
        bint ignore_case
):
    if using:
        for to_be_found in using:
            [
                _maybe_add(processed, method, list_element, to_be_found, ignore_case)
                for list_element in the_list
            ]


cpdef list filter_list_of_strings(
        list the_list,
        tuple must_start_with = None,
        tuple must_end_with = None,
        tuple must_contain = None,
        bint ignore_case = False
):
    if not the_list:
        return the_list

    cdef set processed = set()

    _apply_filters(the_list, processed, must_start_with, str.startswith, ignore_case)
    _apply_filters(the_list, processed, must_end_with, str.endswith, ignore_case)
    _apply_filters(the_list, processed, must_contain, str.__contains__, ignore_case)

    return list(processed)


cpdef bint exists_within_a_list_of_dicts(
        list the_list,
        object key_to_match,
        object value_to_match = _NULL
):
    for item in the_list:
        if key_to_match in item and (
            value_to_match is _NULL or item[key_to_match] == value_to_match
        ):
            return True
    return False


cpdef dict get_within_a_list_of_dicts(
        list the_list,
        object dictionary_key,
        object dictionary_value = _NULL,
        object default_value = _NULL
):
    for item in the_list:
        if (dictionary_key in item and dictionary_value is _NULL) or item.get(
                dictionary_key
        ) == dictionary_value:
            return item

    return default_value or {}


cpdef bint equals(list lhs, list rhs, bint ignore_order = True):
    if not isinstance(lhs, list) or not isinstance(rhs, list):
        return False

    if ignore_order:
        if len(lhs) != len(rhs):
            return False

        if (
                len(lhs) < 37
        ):  # number established with benchmarks. The following gets slower when list is longer than 37
            for item in lhs:
                if item not in rhs:
                    return False
            return True

        return set(lhs) == set(rhs)

    return lhs == rhs


cpdef list expand_right(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    return expand_right_inplace(list(the_list), expansion_size, filler)


cpdef list expand_right_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    if callable(filler):
        the_list.extend([filler(i) for i in range(expansion_size)])
    else:
        the_list.extend([filler for i in range(expansion_size)])
    return the_list


cpdef list expand_left(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    return expand_left_inplace(list(the_list), expansion_size, filler)


cpdef list expand_left_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = None
):
    if callable(filler):
        expansion: list = [filler(i) for i in range(expansion_size)]
    else:
        expansion: list = [filler] * expansion_size

    the_list.insert(0, expansion)
    return the_list


cpdef list generate_random_list_of_ints(
        unsigned int length,
        int min_bound = 0,
        int max_bound = 1_000_000
):
    return [random.randint(min_bound, max_bound) for _ in range(length)]


cpdef list rotate_left(
        list the_list,
        unsigned int rotation_size
):
    return the_list[rotation_size:] + the_list[:rotation_size]


cpdef list rotate_right(
        list the_list,
        unsigned int rotation_size
):
    return the_list[-rotation_size:] + the_list[:-rotation_size]


cpdef list chunk_list(
        list the_list,
        unsigned int chunk_size
):
    return [the_list[i:i + chunk_size] for i in range(0, len(the_list), chunk_size)]


cpdef void append_if(list the_list, bint condition, object value):
    if condition:
        the_list.append(value)
