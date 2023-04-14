"""
Contains some utility method for fuzz
"""

from typing import Union, Optional, Iterable

from rapidfuzz import fuzz_cpp


def get_highest_scoring_string(
        item: str,
        candidates: list[str],
        method: Union[
            fuzz_cpp.ratio,
            fuzz_cpp.token_ratio,
            fuzz_cpp.token_set_ratio,
            fuzz_cpp.token_sort_ratio
        ] = fuzz_cpp.token_sort_ratio) -> Optional[str]:
    """
    Returns the highest fuzz-scoring *item* in *iterable* using the provided *method*
    """

def get_fuzz_average(
    lhs: str,
    rhs: str,
    methods: Iterable[
        Union[fuzz_cpp.token_sort_ratio, fuzz_cpp.token_set_ratio, fuzz_cpp.ratio]
    ] = None,
) -> float:
    """
    Returns the average fuzz ratio of *lhs* and *rhs* using the provided *methods*

    The method uses *lru_cache*.
    """