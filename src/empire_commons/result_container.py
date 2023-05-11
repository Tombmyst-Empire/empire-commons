"""
Module for ResultContainer class.
"""

from __future__ import annotations

from copy import copy
from typing import *

from empire_commons.commons.exceptions import ProgrammingException

SuccessType = TypeVar("SuccessType")
FailType = TypeVar("FailType")


class ResultContainer(Generic[SuccessType, FailType]):
    """
    An object that contains a read-only value.
    """

    __slots__ = ("_ok", "_value", "_cache_hit")

    def __init__(
        self,
        value: Optional[SuccessType | FailType] = None,
        *,
        ok: bool = True,
        cache_hit: bool = False,
    ):
        self._value: Optional[SuccessType | FailType] = value
        self._ok: bool = ok
        self._cache_hit: bool = cache_hit

    @property
    def is_ok(self) -> bool:
        return self._ok

    @property
    def value(self) -> Optional[SuccessType | FailType]:
        return copy(self._value)

    @property
    def cache_hit(self) -> bool:
        return self._cache_hit

    def __bool__(self) -> bool:
        if self._ok:
            return True
        else:
            return False

    def __len__(self) -> int:
        if hasattr(self._value, "__len__"):
            return len(self._value)  # type: ignore
        elif self._value is None:
            return 0
        else:
            raise ProgrammingException(
                f"You tried to call __len__ on a value that does not implement it! Value type: {type(self._value)}"
            )

    def __contains__(self, item: Any) -> bool:
        if hasattr(self._value, "__contains__"):
            return self._value.__contains__(item)  # type: ignore
        elif self._value is None:
            return False
        else:
            raise ProgrammingException(
                f"You tried to call __contains__ on a value that does not implement it! Value type: {type(item)}"
            )
