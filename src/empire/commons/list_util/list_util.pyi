"""
Utility module for lists
"""
from typing import Any, Callable, Sequence, TypeVar

from empire.commons.types_ import _NULL


T = TypeVar('T')


def try_get(the_list: list, index: int, default: Any = None) -> Any:
    """
    Safe get for list.

    If *index* is out of bounds, returns *default*.
    """

def list_contains_sub_list(lhs: list, rhs: list) -> bool:
    """
    Checks if the longest list contains the smallest list. It does not matter which of the two parameters
    is the longest list as this function determines it
    """


def set_contains_sub_list(lhs: set, rhs: set) -> bool:
    """
    Checks if the longest set contains the smallest set. It does not matter which of the two parameters
    is the longest set as this function determines it
    """


def filter_list_of_strings(
        the_list: list,
        *,
        must_start_with: tuple[str, ...] = None,
        must_end_with: tuple[str, ...] = None,
        must_contain: tuple[str, ...] = None,
        ignore_case: bool = False
) -> list:
    """
    Filters and unduplicate a list of strings using the provided conditions.
    :param the_list:
    :param must_start_with: Each string must start with this/these value(s)
    :param must_end_with: Each string must end with this/these value(s)
    :param must_contain: Each string must contain this/these value(s)
    :param ignore_case:
    :return:
    """


def exists_within_a_list_of_dicts(
        the_list: list,
        *,
        key_to_match: Any,
        value_to_match: Any = _NULL
) -> bool:
    """
    Checks if *key_to_match* in any of the dicts of *the_list*.

    Setting a value to *value_to_match* will also check for this to be the value of *key_to_match*.
    """


def get_within_a_list_of_dicts(
        the_list: list,
        *,
        dictionary_key: Any,
        dictionary_value: Any = _NULL,
        default_value: Any = _NULL
) -> dict:
    """
    Returns the first dict that matches either has a key *dictionary_key* and/or, when *dictionary_value* is set,
    has *dictionary_key* set to *dictionary_value*.
    """

def equals(lhs: list, rhs: list, ignore_order: bool = True) -> bool:
    """
    Checks for *lhs* and *rhs* equality. If *ignore_order* is False then both list must be ordered the same
    """


def expand_right(
        the_list: list,
        expansion_size: int,
        *,
        filler: Callable[[int], Any] | Any = None
) -> list:
    """
    Expands to the right (the end of it), the given list
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """


def expand_right_inplace(
        the_list: list,
        expansion_size: int,
        *,
        filler: Callable[[int], Any] | Any = None
) -> list:
    """
    Expands to the right (the end of it), the given list, inplace
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """


def expand_left(
        the_list: list,
        expansion_size: int,
        *,
        filler: Callable[[int], Any] | Any = None
) -> list:
    """
    Expands to the left (the start of it), the given list
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """


def expand_left_inplace(
        the_list: list,
        expansion_size: int,
        *,
        filler: Callable[[int], Any] | Any = None
) -> list:
    """
    Expands to the left (the start of it), the given list, inplace
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """


def generate_random_list_of_ints(
        length: int,
        min_bound: int = 0,
        max_bound: int = 1_000_000
) -> list[int]:
    """
    Generates a list of random integers of length *length*.

    :param length: The number of integers to generate
    :param min_bound: The minimum value an integer can have
    :param max_bound: The maximum value an integer can have
    :return:
    """


def rotate_left(the_list: list, rotation_size: int) -> list:
    """
    Rotates the list to the left by *rotation_size* positions.
    """


def rotate_right(the_list: list, rotation_size: int) -> list:
    """
    Rotates the list to the right by *rotation_size* positions.
    """


def chunk_list(the_list: list[T], chunk_size: int) -> list[Sequence[T]]:
    """
    Chunks *the_list* into sequences of size at-most *chunk_size*.
    """


def append_if(the_list: list[T], condition: bool, value: T):
    """
    Appends *value* to *the_list* if *condition* is true
    """
