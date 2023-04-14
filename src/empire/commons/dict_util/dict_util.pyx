"""
Utility functions for dictionaries and mappings
"""

from typing import Any

cpdef dict swap_key_values(dict the_dict):
    """
    Swap a dictionary keys and values
    """
    return {value: key for key, value in the_dict.items()}


cpdef dict remap(dict the_dict, dict mapping):
    """
    Remaps the given directory using the provided mapping.

    The mapping keys represent the provided dictionary keys and mapping values represent
    the desired keys.
    """
    return {
        mapping.get(key, key): value
        for key, value in the_dict.items()
    }


def get_first_non_null(the_dict: dict, *fields: Any, default: Any = None) -> Any:
    """
    Returns the first non-None value from a sequence of fields of a dictionary.
    If none of the fields returned a non-None value, then the method return *default*.

    """
    for field in fields:
        if the_dict.get(field):
            return the_dict[field]
    return default


cpdef void try_del(dict the_dict, object key):
    """
    Tries to delete a fields from a dictionary.
    """
    try:
        del the_dict[key]
    except KeyError:
        pass
