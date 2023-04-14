from rapidfuzz import fuzz_cpp
from empire.commons.statistics_util cimport avg


cpdef str get_highest_scoring_string(
        str item,
        list candidates,
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


cpdef float get_fuzz_average(
        str lhs,
        str rhs,
        list methods = None
):
    methods = methods or [fuzz_cpp.token_sort_ratio, fuzz_cpp.ratio, fuzz_cpp.token_set_ratio]
    return avg([method(lhs, rhs) for method in methods])
