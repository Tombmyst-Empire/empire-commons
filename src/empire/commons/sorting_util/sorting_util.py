from typing import Any, Iterable, TypeVar

_TypeKey = TypeVar('_TypeKey')
_TypeValue = TypeVar('_TypeValue')
_TypeObject = TypeVar('_TypeObject')


def sort_dict_list_by_another_list(
        to_sort: Iterable[dict[_TypeKey, _TypeValue]],
        using: Iterable[_TypeValue],
        item_key_in_to_sort: _TypeKey
) -> list[dict[_TypeKey, _TypeValue]]:
    """
    Sorts *to_sort*, which must be an iterable of dicts in accordance with list *using*, which must be an iterable of the same type
    than *to_sort* values. *item_key_in_to_sort* should be the key to use for sorting *to_sort*.

    Respects immutability of *to_sort*, this method won't change the provided instance.

    Example: ::

        l = [{'a': 1, 'b': 45}, {'a': 12, 'b': 1}, {'a': 4, 'b': 123}]
        ll = [4, 1, 12]
        print(SortingUtil.sort_dict_list_by_another_list(l, ll, 'a'))

        # >>> [{'a': 4, 'b': 123}, {'a': 1, 'b': 45}, {'a': 12, 'b': 1}]
    """
    order: dict[Any, int] = {value: index for index, value in enumerate(using)}
    return sorted(to_sort, key=lambda x: order[x[item_key_in_to_sort]])

def sort_object_list_by_another_list(to_sort: Iterable[_TypeObject], using: Iterable[Any], item_key_in_to_sort: str) -> list[_TypeObject]:
    """
    See `SortingUtil.sort_dict_list_by_another_list` for a description on how this method works.

    The only difference is on how values are accessed in *to_sort* iterable:

    Instead of using the subscript operator (``[ ]``), this method uses *getattr* to access the attribute's value of the objects contained in
    *to_sort*.
    """
    order: dict[Any, int] = {value: index for index, value in enumerate(using)}
    return sorted(to_sort, key=lambda x: order[getattr(x, item_key_in_to_sort)])


if __name__ == '__main__':
    l = [{'a': 1, 'b': 45}, {'a': 12, 'b': 1}, {'a': 4, 'b': 123}]
    ll = [4, 1, 12]
    print(sort_dict_list_by_another_list(l, ll, 'a'))
