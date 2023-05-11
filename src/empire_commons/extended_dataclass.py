"""
Module for ExtendedDataclass class
"""
from collections import deque
from copy import deepcopy
from dataclasses import is_dataclass, fields
from types import MappingProxyType
from typing import Any, Optional

from bidict import bidict
from frozendict import frozendict

from empire_commons.commons.types_ import JsonType, NULL


class ExtendedDataclass:
    """
    Adds some methods to a dataclass that make them behave sort like a dictionary.

    To use, simply inherit from this class.
    """

    def __contains__(self, key: str) -> bool:
        """
        Return True if dataclass has field *key*, else False.
        """
        return key in self.__dataclass_fields__  # noqa pylint: disable=no-member

    def keys(self) -> tuple[str]:
        """
        Returns a tuple of all dataclass fields
        """
        return tuple(
            self.__dataclass_fields__.keys()
        )  # noqa  pylint: disable=no-member

    def values(self) -> tuple[Any]:
        """
        Returns a tuple of all dataclass values
        """
        return tuple(
            (getattr(self, key) for key in self.__dataclass_fields__.keys())
        )  # noqa  pylint: disable=no-member

    def items(self) -> MappingProxyType[str, Any]:
        """
        Returns key value pairs of the dataclass
        """
        return MappingProxyType(
            {key: getattr(self, key) for key in self.__dataclass_fields__.keys()}
        )  # noqa   pylint: disable=no-member

    def __getitem__(self, key: str) -> Any:
        """
        Returns the value of field *key*
        """
        return getattr(self, key)

    def to_json(self) -> JsonType:
        return to_json(self)

    def diff(self, other: Any) -> Optional[dict[str, tuple[Any, Any]]]:
        """
        Performs a diff between two dataclasses and returns a dictionary of the differences.

        The keys of the dictionary are the field names of the dataclasses, the values are tuples of the values of the fields where
        the first value is the value of the field in the current dataclass and the second value is the value of the field in the other dataclass.
        """
        if not isinstance(other, self.__class__):
            raise TypeError(f'Cannot diff {self.__class__} with {type(other)}')

        if not is_dataclass(self):
            raise TypeError(f'Self {self.__class__} is not a dataclass')

        modified: dict[str, tuple[Any, Any]] = {}

        for field in fields(self):  # noqa
            if getattr(self, field.name) != getattr(other, field.name):
                modified[field.name] = (getattr(self, field.name), getattr(other, field.name))

        return modified or None


def to_json(obj: Any) -> JsonType:
    """
    Similar to builtin dataclasses.as_dict is that it also handles
    frozendicts, bimaps and other types that Empire supports and
    returns JSON-compatible data.

    .. note :: ORJSON handles dataclass serialization
    """
    if is_dataclass(obj):
        result = []
        for a_field in fields(obj):
            value = to_json(getattr(obj, a_field.name))
            if value != NULL:
                result.append((a_field.name, value))
        return dict(result)
    elif isinstance(obj, (list, tuple, set, frozenset, deque)):
        return [to_json(item) for item in obj if item != NULL]
    elif isinstance(obj, (dict, frozendict, bidict)):
        return {to_json(key): to_json(value) for key, value in obj.items() if value != NULL}
    else:
        return deepcopy(obj)

