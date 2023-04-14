from collections import defaultdict, OrderedDict
from typing import Any

from frozendict import frozendict


__all__ = [
    'is_container',
    'is_dict',
    'is_sequence',
    'is_empty',
    'is_mutable',
    'get_type_name'
]


def is_container(value: Any) -> bool:
    return isinstance(value, (dict, list, tuple, set, frozenset, frozendict))

def is_dict(value: Any) -> bool:
    return isinstance(value, (dict, frozendict, defaultdict, OrderedDict))

def is_sequence(value: Any) -> bool:
    return isinstance(value, (list, tuple, set, frozenset))

def is_empty(value: Any) -> bool:
    """
    Returns True if *value* is None or has __len__ defined and has length of 0,
    False otherwise.
    """
    return value is None or (hasattr(value, "__len__") and len(value) == 0)

def is_mutable(value: Any) -> bool:
    """
    Returns True if *value* is mutable, False otherwise.
    """
    return isinstance(value, (list, dict, set))

def get_type_name(value: Any) -> str:
    return type(value).__name__
