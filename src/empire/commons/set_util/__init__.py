from typing import TypeVar

from empire.commons.core.core import set_util_contains_sub_set


T = TypeVar('T')


def contains_sub_set(lhs: set[T], rhs: set[T]) -> bool:
    """
    Checks if the longest set contains the smallest set. It does not matter which of the two parameters
    is the longest set as this function determines it
    """
    return set_util_contains_sub_set(lhs, rhs)
