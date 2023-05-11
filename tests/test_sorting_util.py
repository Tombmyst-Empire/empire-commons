from dataclasses import dataclass

import pytest

from empire_commons.commons import sorting_util


def test_sort_dict_list_by_another_list():
    l1 = [{'a': 1, 'b': 45}, {'a': 12, 'b': 1}, {'a': 4, 'b': 123}]
    l2 = [4, 1, 12]
    l3 = [123, 1, 45]
    l4 = [45, 1, 123]

    assert sorting_util.sort_dict_list_by_another_list(
        l1,
        l2,
        'a'
    ) == [{'a': 4, 'b': 123}, {'a': 1, 'b': 45}, {'a': 12, 'b': 1}]

    assert sorting_util.sort_dict_list_by_another_list(
        l1,
        l3,
        'b'
    ) == [{'a': 4, 'b': 123}, {'a': 12, 'b': 1}, {'a': 1, 'b': 45}]

    assert sorting_util.sort_dict_list_by_another_list(
        l1,
        l4,
        'b'
    ) == l1

    with pytest.raises(KeyError):
        sorting_util.sort_dict_list_by_another_list(
            l1, l2, 'rogers'
        )


def test_sort_object_list_by_another_list():
    @dataclass
    class Dummy:
        a: int
        b: int

    l1 = [Dummy(2, 46), Dummy(13, 2), Dummy(6, -123)]
    l2 = [6, 2, 13]
    l3 = [46, -123, 2]
    l4 = [2, 13, 6]

    assert sorting_util.sort_object_list_by_another_list(
        l1,
        l2,
        'a'
    ) == [Dummy(6, -123), Dummy(2, 46), Dummy(13, 2)]

    assert sorting_util.sort_object_list_by_another_list(
        l1,
        l3,
        'b'
    ) == [Dummy(2, 46), Dummy(6, -123), Dummy(13, 2)]

    assert sorting_util.sort_object_list_by_another_list(
        l1,
        l4,
        'a'
    ) == l1

    with pytest.raises(AttributeError):
        sorting_util.sort_object_list_by_another_list(
            l1, l2, 'rogers'
        )
