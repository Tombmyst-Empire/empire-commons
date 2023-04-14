import pytest

from empire.commons.slice_util import slice_is_in, slice_contains_slice, \
    get_slice_object_with_most_coverage, slice_from_string


def test_is_in_with_none_inputs():
    with pytest.raises(TypeError):
        assert not slice_is_in(None, 1)
        assert not slice_is_in(slice(0, 10), None)
        assert not slice_is_in(None, None)


def test_is_in():
    assert slice_is_in(slice(0, 10), 5)
    assert not slice_is_in(slice(0, 10), 10)
    assert slice_is_in(slice(0, 10), 10, inclusive=True)


def test_slice_contains_slice():
    assert slice_contains_slice(slice(0, 10), slice(0, 2))
    assert slice_contains_slice(slice(0, 10), slice(6, 9))
    assert not slice_contains_slice(slice(0, 10), slice(-1, 11))
    assert not slice_contains_slice(slice(0, 10), slice(8, 10))


def test_get_slice_object_with_most_coverage():
    assert get_slice_object_with_most_coverage(
        slice(4, 11), slice(0, 9), slice(10, 49)
    ) == slice(0, 9)


def test_from_string():
    assert (
        slice_from_string("", 0)
        == slice_from_string("1", 0)
        == slice_from_string("1:2:3:4", 0)
        is None
    )
    assert slice_from_string("1:2:3", 10) == slice(1, 2, 3)
    assert slice_from_string("4:5", 10) == slice(4, 5)
