from rapidfuzz import fuzz_cpp


cpdef str get_highest_scoring_string(
        str item,
        list candidates,
        object method = *
)

cpdef float get_fuzz_average(
        str lhs,
        str rhs,
        list methods = *
)
