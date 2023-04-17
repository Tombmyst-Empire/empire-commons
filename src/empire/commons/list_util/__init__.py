from typing import TypeVar, Any, Sequence

from empire.commons.core.core import (
    list_util_try_get,
    list_util_equals,
    list_util_chunk_list,
    list_util_append_if,
    list_util_expand_left,
    list_util_rotate_left,
    list_util_expand_right,
    list_util_rotate_right,
    list_util_contains_sub_list,
    list_util_filter_list_of_strings,
    list_util_expand_left_inplace,
    list_util_expand_right_inplace,
    list_util_generate_random_list_of_ints,
    list_util_filter_list_of_strings
)

T = TypeVar('T')


def try_get(the_list: list, index: int, default_value: T = None) -> T:
    """
    Safe get for list.

    If *index* is out of bounds, returns *default*.
    """
    return list_util_try_get(the_list, index, default_value)


def contains_sub_list(lhs: list[T], rhs: list[T]) -> bool:
    """
    Checks if the longest list contains the smallest list. It does not matter which of the two parameters
    is the longest list as this function determines it
    """
    return list_util_contains_sub_list(lhs, rhs)


def filter_list_of_strings(
    the_list: list[str],
    must_start_with: tuple[str, ...] | None = None,
    must_end_with: tuple[str, ...] | None = None,
    must_contain: tuple[str, ...] | None = None,
    ignore_case: bool = False
) -> list[str]:
    """
    Filters and unduplicate a list of strings using the provided conditions.
    :param the_list:
    :param must_start_with: Each string must start with this/these value(s)
    :param must_end_with: Each string must end with this/these value(s)
    :param must_contain: Each string must contain this/these value(s)
    :param ignore_case:
    :return:
    """
    return list_util_filter_list_of_strings(
        the_list,
        must_start_with,
        must_end_with,
        must_contain,
        ignore_case
    )


def equals(lhs: list, rhs: list, ignore_order: bool = True) -> bool:
    """
    Checks for *lhs* and *rhs* equality. If *ignore_order* is False then both list must be ordered the same
    """
    return list_util_equals(lhs, rhs, ignore_order)


def expand_right(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
    """
    Expands to the right (the end of it), the given list
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """
    return list_util_expand_right(the_list, expansion_size, filler)


def expand_right_inplace(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
    """
    Expands to the right (the end of it), the given list, inplace
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """
    return list_util_expand_right_inplace(the_list, expansion_size, filler)


def expand_left(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
    """
    Expands to the left (the start of it), the given list
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """
    return list_util_expand_left(the_list, expansion_size, filler)


def expand_left_inplace(the_list: list, expansion_size: int, filler: Any = None) -> list:
    """
    Expands to the left (the start of it), the given list, inplace
    :param the_list: The list
    :param expansion_size: Size to expand
    :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
    :return: The new list
    """
    return list_util_expand_left_inplace(the_list, expansion_size, filler)


def generate_random_list_of_ints(length: int, min_bound: int = 0, max_bound: int = 1_000_000) -> list[int]:
    """
    Generates a list of random integers of length *length*.

    :param length: The number of integers to generate
    :param min_bound: The minimum value an integer can have
    :param max_bound: The maximum value an integer can have
    :return:
    """
    list_util_generate_random_list_of_ints(length, min_bound, max_bound)


def rotate_left(the_list: list[T], rotation_size: int) -> list[T]:
    """
    Rotates the list to the left by *rotation_size* positions.
    """
    return list_util_rotate_left(the_list, rotation_size)


def rotate_right(the_list: list[T], rotation_size: int) -> list[T]:
    """
    Rotates the list to the right by *rotation_size* positions.
    """
    return list_util_rotate_right(the_list, rotation_size)


def chunk_list(the_list: list[T], chunk_size: int) -> list[Sequence[T]]:
    """
    Chunks *the_list* into sequences of size at-most *chunk_size*.
    """
    return list_util_chunk_list(the_list, chunk_size)


def append_if(the_list: list[T], condition: bool, value: T):
    """
    Appends *value* to *the_list* if *condition* is true
    """
    return list_util_append_if(the_list, condition, value)

def zip_flattened(*items_to_zip: list) -> list:
    """
    As doing ``zip(list1, list2)`` will create a list of tuples, this function performs the zip operation
    and flattens the list.

    Example: ::

        l = [1, 3, 5]
        ll = [2, 4, 6]
        print(ListUtil.zip_flattened(l, ll))

        # >>> [1, 2, 3, 4, 5, 6]
        # instead of:
        # [(1, 2), (3, 4), (5, 6)]
    """
    return [sub_zip for zipped in zip(*items_to_zip) for sub_zip in zipped]
