cpdef object try_get(list the_list, unsigned int index, object default_value = *)
cpdef bint list_contains_sub_list(list lhs, list rhs)
cpdef bint set_contains_sub_list(set lhs, set rhs)
cdef inline void _maybe_add(
        set processed,
        object method,
        str list_element,
        str to_be_found,
        bint ignore_case
)
cdef inline void _apply_filters(
        list the_list,
        set processed,
        tuple using,
        object method,
        bint ignore_case
)
cpdef list filter_list_of_strings(
        list the_list,
        tuple must_start_with = *,
        tuple must_end_with = *,
        tuple must_contain = *,
        bint ignore_case = *
)
cpdef bint exists_within_a_list_of_dicts(
        list the_list,
        object key_to_match,
        object value_to_match = *
)
cpdef dict get_within_a_list_of_dicts(
        list the_list,
        object dictionary_key,
        object dictionary_value = *,
        object default_value = *
)
cpdef bint equals(list lhs, list rhs, bint ignore_order = *)
cpdef list expand_right(
        list the_list,
        unsigned int expansion_size,
        object filler = *
)
cpdef list expand_right_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = *
)
cpdef list expand_left(
        list the_list,
        unsigned int expansion_size,
        object filler = *
)
cpdef list expand_left_inplace(
        list the_list,
        unsigned int expansion_size,
        object filler = *
)
cpdef list generate_random_list_of_ints(
        unsigned int length,
        int min_bound = *,
        int max_bound = *
)
cpdef list rotate_left(
        list the_list,
        unsigned int rotation_size
)
cpdef list rotate_right(
        list the_list,
        unsigned int rotation_size
)

cpdef list chunk_list(
        list the_list,
        unsigned int chunk_size
)

cpdef void append_if(list the_list, bint condition, object value)