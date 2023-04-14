"""
Utility functions for lists of dicts.
"""
from typing import TypeVar

T = TypeVar('T')

def only_keep_these_root_keys(the_list: list, *keys) -> list:
    """
    Return a list of dictionaries with only *keys* as keys.
    """

def create_dict_from_list_of_dicts(the_list: list[dict], key: str) -> dict[str, dict]:
    """
    Create a dictionary from a list of dictionaries.
    """


def create_dict_from_list_of_objects(the_list: list[T], key: str) -> dict[str, T]:
    """
    Create a dictionary from a list of dictionaries.
    """
