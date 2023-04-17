from typing import TypeVar, Any

from empire.commons.types_ import NULL

from empire.commons.core.core import (
    list_dict_util_keep_root_keys,
    list_dict_util_create_dict_from_list_of_dicts,
    list_dict_util_create_dict_from_list_of_objects,
    list_dict_util_exists_within_a_list_of_dicts,
    list_dict_util_get_within_a_list_of_dicts
)


T = TypeVar('T')


def keep_root_keys(the_list: list[dict], *keys) -> list[dict]:
    """
    Return a list of dictionaries with only *keys* as keys.
    """
    return list_dict_util_keep_root_keys(the_list, *keys)


def create_dict_from_list_of_dicts(the_list: list[dict], key: str) -> dict[str, dict]:
    """
    Create a dictionary from a list of dictionaries.
    """
    return list_dict_util_create_dict_from_list_of_dicts(
        the_list, key
    )


def create_dict_from_list_of_objects(the_list: list[T], key: str) -> dict[str, T]:
    """
    Create a dictionary from a list of objects.
    """
    return list_dict_util_create_dict_from_list_of_objects(the_list, key)


def exists_within_a_list_of_dicts(the_list: list[dict], key_to_match: Any, value_to_match: Any = NULL) -> bool:
    """
    Checks if *key_to_match* in any of the dicts of *the_list*.

    Setting a value to *value_to_match* will also check for this to be the value of *key_to_match*.
    """
    return list_dict_util_exists_within_a_list_of_dicts(
        the_list,
        key_to_match,
        value_to_match
    )


def get_within_a_list_of_dicts(
    the_list: list[dict],
    dictionary_key: Any,
    dictionary_value: Any = NULL,
    default_value: Any = NULL
) -> bool:
    """
    Returns the first dict that matches either has a key *dictionary_key* and/or, when *dictionary_value* is set,
    has *dictionary_key* set to *dictionary_value*.
    """
    return list_dict_util_get_within_a_list_of_dicts(
        the_list,
        dictionary_key,
        dictionary_value,
        default_value
    )
