cdef class Vec2D:
    cdef public double x
    cdef public double y

    cdef inline bint is_nan(self)

# ========================================================================================================================== MATH UTIL
cpdef double math_util_avg(tuple data)
cpdef int math_util_clamp_int(int number, int minimum, int maximum)
cpdef float math_util_clamp_float(double number, double minimum, double maximum)

# ========================================================================================================================== DICT UTIL

cpdef dict dict_util_swap_key_values(dict the_dict)
cpdef dict dict_util_remap(dict the_dict, dict mapping)
cpdef dict_util_get_first_non_null(dict the_dict, tuple fields, default = *)
cpdef dict dict_util_try_del(dict the_dict, object key)

# ========================================================================================================================== FUZZ UTIL

cpdef str fuzz_util_get_highest_scoring_string(str item, tuple candidates, object method = *)
cpdef double fuzz_util_get_fuzz_average(str lhs, str rhs, tuple methods)

# ========================================================================================================================== LIST DICT UTIL

cpdef list list_dict_util_keep_root_keys(list the_list, tuple keys)
cpdef dict list_dict_util_create_dict_from_list_of_dicts(list the_list, str key)
cpdef dict list_dict_util_create_dict_from_list_of_objects(list the_list, str key)
cpdef bint list_dict_util_exists_within_a_list_of_dicts(list the_list, object key_to_match, object value_to_match = *)
cpdef dict list_dict_util_get_within_a_list_of_dicts(list the_list, object dictionary_key, object dictionary_value = *, object default_value = *)

# ========================================================================================================================== LIST UTIL

cdef inline void _list_util_maybe_add(set processed, object method, str list_element, str to_be_found, bint ignore_case)
cdef inline void _list_util_apply_filters(list the_list, set processed, tuple using, object method, bint ignore_case)
cpdef object list_util_try_get(list the_list, unsigned int index, object default_value = *)
cpdef bint list_util_contains_sub_list(list lhs, list rhs)
cpdef list list_util_filter_list_of_strings(list the_list, tuple must_start_with = *, tuple must_end_with = *, tuple must_contain = *, bint ignore_case = *)
cpdef bint list_util_equals(list lhs, list rhs, bint ignore_order = *)
cpdef list list_util_expand_right(list the_list, unsigned int expansion_size, object filler = *)
cpdef list list_util_expand_right_inplace(list the_list, unsigned int expansion_size, object filler = *)
cpdef list list_util_expand_left(list the_list, unsigned int expansion_size, object filler = *)
cpdef list list_util_expand_left_inplace(list the_list, unsigned int expansion_size, object filler = *)
cpdef list list_util_generate_random_list_of_ints(unsigned int length, int min_bound = *, int max_bound = *)
cpdef list list_util_rotate_left(list the_list, unsigned int rotation_size)
cpdef list list_util_rotate_right(list the_list, unsigned int rotation_size)
cpdef list list_util_chunk_list(list the_list, unsigned int chunk_size)
cpdef void list_util_append_if(list the_list, bint condition, object value)

cpdef list list_util_merge_lists(list lists)

# ========================================================================================================================== NUMBER UTIL

cpdef int number_util_to_int(str s, int default = *, bint strip_non_numeric_chars = *)

# ========================================================================================================================== SET UTIL

cpdef bint set_util_contains_sub_set(set lhs, set rhs)

# ========================================================================================================================== SLICE UTIL

cpdef bint slice_util_number_is_in(slice slice_obj, int number, bint inclusive = *)
cpdef bint slice_util_contains(slice containing_slice, slice slice_to_be_contained)
cpdef slice slice_util_get_slice_with_most_coverage(slice reference_slice, slice slice_a, slice slice_b)
cpdef Vec2D slice_util_get_slice_coverage(slice reference_slice, slice slice_a, slice slice_b)

# ========================================================================================================================== STRING CASING

cpdef str string_casing_to_camel_case_strip_spaces(str the_string)
cpdef str string_casing_to_camel_case_with_underscores(str the_string)
cpdef str string_casing_to_pascal_case_strip_spaces(str the_string)
cpdef str string_casing_to_pascal_case_with_underscores(str the_string)
cpdef str string_casing_to_upper_case_with_underscores(str the_string)

# ========================================================================================================================== TUPLE UTIL

cpdef object tuple_util_try_get(tuple the_tuple, unsigned int index, object default_value = *)
cpdef bint tuple_util_tuple_contains_sub_tuple(tuple lhs, tuple rhs)
