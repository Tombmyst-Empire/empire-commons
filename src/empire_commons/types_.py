from typing import Union, Any


__all__ = [
    'NumberType',
    'JsonType',
    'FrozenJson',
    'ListLikeType',
    'StringListLikeType',
    'DictListLikeType',
    'FileDescriptor',
    'NULL'
]


class _FileDescriptor:
    pass


NumberType = Union[int, float]
_JSON = Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]], list[Union[str, int, float, bool, None, dict[str, Union[str, int, float, bool, None, dict[str, Any], list[Any]]], list[Union[str, int, float, bool, None, dict[str, Any], list[Any]]]]]]]]]]]]
JsonType = Union[str, int, float, bool, None, dict[str, _JSON], list[_JSON]]
JsonList = list[JsonType]
FrozenJson = "FrozenDict[str, Any]"
ListLikeType = list | tuple | set | frozenset
StringListLikeType = list[str] | tuple[str] | set[str] | frozenset[str]
DictListLikeType = list[dict] | tuple[dict] | set[dict] | frozenset[dict]
FileDescriptor = _FileDescriptor | int


class _NULL:
    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def __eq__(self, other):
        return isinstance(other, _NULL)

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "NULL"

    def __repr__(self):
        return "NULL"

    def __hash__(self) -> int:
        return 0


NULL = _NULL()
