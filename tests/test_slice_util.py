import pytest

from empire_commons import slice_util

def test_is_in_with_none_inputs():
    with pytest.raises(TypeError):
        assert not slice_util.number_is_in(None, 1)
        assert not slice_util.number_is_in(slice(0, 10), None)
        assert not slice_util.number_is_in(None, None)


def test_is_in():
    assert slice_util.number_is_in(slice(0, 10), 5)
    assert not slice_util.number_is_in(slice(0, 10), 10)
    assert slice_util.number_is_in(slice(0, 10), 10, inclusive=True)


def test_slice_contains_slice():
    assert slice_util.contains(slice(0, 10), slice(0, 2))
    assert slice_util.contains(slice(0, 10), slice(6, 9))
    assert not slice_util.contains(slice(0, 10), slice(-1, 11))
    assert not slice_util.contains(slice(0, 10), slice(8, 10))


def test_get_slice_object_with_most_coverage():
    assert slice_util.get_slice_with_most_coverage(
        slice(4, 11), slice(0, 9), slice(10, 49)
    ) == slice(0, 9)


def test_from_string():
    assert (
        slice_util.from_string("")
        == slice_util.from_string("1:2:3:4")
        == slice(None, None, None)
    )
    assert slice_util.from_string("1") == slice(None, 1, None)
    assert slice_util.from_string("1:2:3") == slice(1, 2, 3)
    assert slice_util.from_string("4:5") == slice(4, 5)
