from typing import Union, Callable

from rapidfuzz import fuzz_cpp

from empire.commons.core.core import (
    fuzz_util_get_highest_scoring_string,
    fuzz_util_get_fuzz_average
)


def get_highest_scoring_string(
    item: str,
    *candidates: str,
    method: Union[
        fuzz_cpp.ratio,
        fuzz_cpp.token_ratio,
        fuzz_cpp.token_set_ratio,
        fuzz_cpp.token_sort_ratio
    ] = fuzz_cpp.token_sort_ratio
) -> str:
    """
    Returns the highest fuzz-scoring *item* in *iterable* using the provided *method*
    """
    return fuzz_util_get_highest_scoring_string(item, candidates, method)


def get_fuzz_average(
    lhs: str,
    rhs: str,
    *methods: Callable[[str, str], float]
) -> float:
    """
    Returns the average fuzz ratio of *lhs* and *rhs* using the provided *methods*
    """
    methods = tuple(methods)
    return fuzz_util_get_fuzz_average(lhs, rhs, methods)
