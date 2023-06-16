from contextlib import suppress
from typing import Any, Final

from empire_commons import list_util
from empire_commons.exceptions import UnexpectedException
from empire_commons.type_util import get_type_name

_system_keys: list[str] = ['__module__', '__dict__', '__weakref__', '__doc__', '__annotations__']


def _value_to_string(val: Any) -> str:
    if isinstance(val, str):
        return


def list_attributes_names(obj: object) -> list[str]:
    result: list[str] = []

    with suppress(AttributeError):
        result.extend([key for key in obj.__dict__])

    with suppress(AttributeError):
        result.extend([slot for slot in obj.__slots__])

    return result


def list_attributes_values(obj: object) -> list[Any]:
    result: list[Any] = []

    with suppress(AttributeError):
        result.extend([value for value in obj.__dict__.values()])

    with suppress(AttributeError):
        result.extend([getattr(obj, slot) for slot in obj.__slots__])

    return result


def list_instance_classvars_names(obj: object) -> list[str]:
    result: list[str] = []

    with suppress(AttributeError):
        result.extend([key for key in obj.__class__.__dict__ if key not in _system_keys])

    return result


def list_instance_classvars_values(obj: object) -> list[Any]:
    result: list[str] = []

    with suppress(AttributeError):
        result.extend([value for key, value in obj.__class__.__dict__.items() if key not in _system_keys])

    return result


def equals(lhs: Any, rhs: Any) -> bool:
    return (
        isinstance(lhs, type(rhs)) and
        list_util.equals(list_attributes_names(lhs), list_attributes_names(rhs)) and
        list_util.equals(list_attributes_values(lhs), list_attributes_values(rhs))
    )


def to_string(obj: object) -> str:
    join_token: Final[str] = '\n\t'
    classvar_names: list[str] = list_instance_classvars_names(obj)
    classvar_values: list[Any] = list_instance_classvars_values(obj)
    attribute_names: list[str] = list_attributes_names(obj)
    attribute_values: list[Any] = list_attributes_values(obj)

    if len(classvar_names) != len(classvar_values):
        raise UnexpectedException(f'Classvar names and values size are different: {len(classvar_names)} != {len(classvar_values)}')

    if len(attribute_names) != len(attribute_values):
        raise UnexpectedException(f'Classvar names and values size are different: {len(classvar_names)} != {len(classvar_values)}')

    return f'''{get_type_name(obj)} (\n\t
{}'''
