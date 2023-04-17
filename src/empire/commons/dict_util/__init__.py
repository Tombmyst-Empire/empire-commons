from typing import Protocol, TypeVar

from empire.commons.core.core import (
    dict_util_remap,
    dict_util_try_del,
    dict_util_swap_key_values,
    dict_util_get_first_non_null
)

T = TypeVar('T')
U = TypeVar('U')


class _GetItem(Protocol):
    def __getitem__(self, key): ...


def remap(the_dict: dict[T, U], key_map: dict | _GetItem) -> dict[T, U]:
    return dict_util_remap(the_dict, key_map)


def try_del(the_dict: dict[T, U], key: T) -> None:
    return dict_util_try_del(the_dict, key)


def swap_keys_values(the_dict: dict[T, U]) -> dict[U, T]:
    return dict_util_swap_key_values(the_dict)


def get_first_not_null(the_dict: dict[T, U], *fields: T, default: U | None = None) -> U | None:
    return dict_util_get_first_non_null(the_dict, fields, default)
