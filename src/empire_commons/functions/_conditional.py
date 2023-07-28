"""
Conditional helper functions and shortcuts
"""
from enum import Enum
from typing import Any, TypeVar, Type

T = TypeVar('T')


def maybe_enum(value: Enum | Any) -> Any | None:
    """
    If *value* is an Enum, returns *value*.value. Else **None**
    """
    return value.value if value and isinstance(value, Enum) else None


def default(value: T, default_: Any, *, none_only: bool = True) -> T | Any:
    """
    Returns *value* only if *value* is not None,
    returns *default_* otherwise.

    If *none_only* is set to False, any falsy *value* will
    return *default_*
    """
    if none_only:
        return default_ if value is None else value
    else:
        return value if value else default_


def coalesce(*items: Any) -> Any | None:
    """
    Returns first non-None value from *items*
    """
    for item in items:
        if item is not None:
            return item

    return None


def or_raise(value: T, exception_type: Type[Exception], *exception_args, **exception_kwargs) -> T:
    """
    Returns *value* if not None otherwise, raises *exception_type with provided args + kwargs.
    """
    if value is None:
        raise exception_type(*exception_args, **exception_kwargs)

    return value


def or_raise_broad(value: T, exception_type: Type[Exception], *exception_args, **exception_kwargs) -> T:
    """
    Returns *value* if it is a truthy value, otherwise, raises *exception_type with provided args + kwargs.
    """

    if not value:
        raise exception_type(*exception_args, **exception_kwargs)

    return value