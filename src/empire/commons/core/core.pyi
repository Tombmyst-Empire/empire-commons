from asyncio import Protocol
from typing import Any, Callable, TypeVar, Union, Sequence

from rapidfuzz import fuzz_cpp

from empire.commons.types_ import NumberType, NULL
from empire.commons.vector.vec2d import Vec2D

T = TypeVar('T')
U = TypeVar('U')

class _GetItem(Protocol):
    def __getitem__(self, key): ...

# ========================================================================================================================== MATH UTIL

def math_util_avg(*data: NumberType) -> float: ...
def math_util_clamp_int(number: int, minimum: int, maximum: int) -> int:
        """
        Clamps integer *number* between *minimum* and *maximum*
        """
def math_util_clamp_float(number: float, minimum: float, maximum: float) -> float:
        """
        Clamps float *number* between *minimum* and *maximum*
        """

# ========================================================================================================================== DICT UTIL

def dict_util_swap_key_values(the_dict: dict[T, U]) -> dict[U, T]: ...

def dict_util_remap(the_dict: dict[T, U], key_map: dict | _GetItem) -> dict[T, U]: ...

def dict_util_get_first_non_null(the_dict: dict[T, U], *fields: T, default: U | None = None) -> U | None: ...

def dict_util_try_del(the_dict: dict[T, U], key: T) -> None: ...

# ========================================================================================================================== FUZZ UTIL

def fuzz_util_get_highest_scoring_string(
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

def fuzz_util_get_fuzz_average(lhs: str, rhs: str, *methods: Callable[[str, str], float]) -> float:
        """
        Returns the average fuzz ratio of *lhs* and *rhs* using the provided *methods*
        """

# ========================================================================================================================== LIST DICT UTIL

def list_dict_util_keep_root_keys(the_list: list[dict], *keys) -> list[dict]:
        """
        Return a list of dictionaries with only *keys* as keys.
        """
def list_dict_util_create_dict_from_list_of_dicts(the_list: list[dict], key: str) -> dict[str, dict]:
        """
        Create a dictionary from a list of dictionaries.
        """
def list_dict_util_create_dict_from_list_of_objects(the_list: list[T], key: str) -> dict[str, T]:
        """
        Create a dictionary from a list of objects.
        """
def list_dict_util_exists_within_a_list_of_dicts(the_list: list[dict], key_to_match: Any, value_to_match: Any= NULL) -> bool:
        """
        Checks if *key_to_match* in any of the dicts of *the_list*.

        Setting a value to *value_to_match* will also check for this to be the value of *key_to_match*.
        """
def list_dict_util_get_within_a_list_of_dicts(
        the_list: list[dict],
        dictionary_key: Any,
        dictionary_value: Any = NULL,
        default_value: Any = NULL
) -> bool:
        """
        Returns the first dict that matches either has a key *dictionary_key* and/or, when *dictionary_value* is set,
        has *dictionary_key* set to *dictionary_value*.
        """

# ========================================================================================================================== LIST UTIL

def list_util_try_get(the_list: list, index: int, default_value: T = None) -> T:
        """
        Safe get for list.

        If *index* is out of bounds, returns *default*.
        """
def list_util_contains_sub_list(lhs: list[T], rhs: list[T]) -> bool:
        """
        Checks if the longest list contains the smallest list. It does not matter which of the two parameters
        is the longest list as this function determines it
        """
def list_util_filter_list_of_strings(
        the_list: list[str],
        must_start_with: tuple[str, ...] | None= None,
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
def list_util_equals(lhs: list, rhs: list, ignore_order: bool = True) -> bool:
        """
        Checks for *lhs* and *rhs* equality. If *ignore_order* is False then both list must be ordered the same
        """
def list_util_expand_right(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
        """
        Expands to the right (the end of it), the given list
        :param the_list: The list
        :param expansion_size: Size to expand
        :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
        :return: The new list
        """
def list_util_expand_right_inplace(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
        """
        Expands to the right (the end of it), the given list, inplace
        :param the_list: The list
        :param expansion_size: Size to expand
        :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
        :return: The new list
        """
def list_util_expand_left(the_list: list[T], expansion_size: int, filler: Any = None) -> list[T]:
        """
        Expands to the left (the start of it), the given list
        :param the_list: The list
        :param expansion_size: Size to expand
        :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
        :return: The new list
        """
def list_util_expand_left_inplace(the_list: list, expansion_size: int, filler: Any = None) -> list:
        """
        Expands to the left (the start of it), the given list, inplace
        :param the_list: The list
        :param expansion_size: Size to expand
        :param filler: Item to use to fill the expansion. If is a callable, it must have an integer as input parameter and returns something.
        :return: The new list
        """
def list_util_generate_random_list_of_ints(length: int, min_bound: int = 0, max_bound: int = 1_000_000) -> list[int]:
        """
        Generates a list of random integers of length *length*.

        :param length: The number of integers to generate
        :param min_bound: The minimum value an integer can have
        :param max_bound: The maximum value an integer can have
        :return:
        """
def list_util_rotate_left(the_list: list[T], rotation_size: int) -> list[T]:
        """
        Rotates the list to the left by *rotation_size* positions.
        """

def list_util_rotate_right(the_list: list[T], rotation_size: int) -> list[T]:
        """
        Rotates the list to the right by *rotation_size* positions.
        """

def list_util_chunk_list(the_list: list[T], chunk_size: int) -> list[Sequence[T]]:
    """
    Chunks *the_list* into sequences of size at-most *chunk_size*.
    """


def list_util_append_if(the_list: list[T], condition: bool, value: T):
    """
    Appends *value* to *the_list* if *condition* is true
    """


# ========================================================================================================================== NUMBER UTIL

def number_util_to_int(s: str, default: int = 0, strip_non_numeric_chars: bool = False) -> int:
        """
        Tries to cast an integer-like string to an integer by removing, if *strip_non_numeric_chars* is True,
        characters that are not numbers nor constituents of a number (does not discriminate integers from floats).

        If the method is unable to do the operation, it returns *default*.
        """

# ========================================================================================================================== SET UTIL

def set_util_contains_sub_set(lhs: set[T], rhs: set[T]) -> bool:
        """
        Checks if the longest set contains the smallest set. It does not matter which of the two parameters
        is the longest set as this function determines it
        """

# ========================================================================================================================== SLICE UTIL

def slice_util_number_is_in(slice_obj: slice, number: int, inclusive: bool = False) -> bool:
        """
        Returns True if *number* is contained within *slice_obj*.
        """
def slice_util_contains(containing_slice: slice, slice_to_be_contained: slice) -> bool:
        """
        Returns True if *slice_to_be_contained* is contained within *containing_slice*.
        """
def slice_util_get_slice_with_most_coverage(reference_slice: slice, slice_a: slice, slice_b: slice) -> slice:
        """
        Returns the slice object with the most coverage.

        Example:

        You have 2 slices: (0, 10) and (10, 20). Reference slice is (8, 18), then
        the slice with most coverage would be the second.
        """
def slice_util_get_slice_coverage(reference_slice: slice, slice_a: slice, slice_b: slice) -> Vec2D:
        """
        Computes the coverage score for *slice_a* and *slice_b* on *reference_slice*.
        
        Returns a Vec2D where X is the coverage score for *slice_a* and Y is the coverage
        score for *slice_b*.
        """

# ========================================================================================================================== STRING CASING

def string_casing_to_camel_case_strip_spaces(the_string: str) -> str: ...
def string_casing_to_camel_case_with_underscores(the_string: str) -> str: ...
def string_casing_to_pascal_case_strip_spaces(the_string: str) -> str: ...
def string_casing_to_pascal_case_with_underscores(the_string: str) -> str: ...
def string_casing_to_upper_case_with_underscores(the_string: str) -> str: ...

# ========================================================================================================================== TUPLE UTIL

def tuple_util_try_get(the_tuple: tuple[T], index: int, default_value: T | None = None) -> T | None: ...
def tuple_util_tuple_contains_sub_tuple(lhs: tuple[T], rhs: tuple[T]) -> bool: ...
