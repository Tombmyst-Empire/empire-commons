import pytest

from empire.commons.dict_util import swap_key_values, remap, get_first_non_null, try_del


def test_swap_key_values():
    dict_ = {"a": 1, "b": 2, "c": None, None: "d"}
    swapped = swap_key_values(dict_)

    assert dict_ == {
        "a": 1,
        "b": 2,
        "c": None,
        None: "d",
    }, "original dict must be unchanged"
    assert swapped == {1: "a", 2: "b", None: "c", "d": None}


def test_swap_key_values_with_multiple_same_values():
    dict_ = {"a": 1, "b": 1, "c": 1, "d": 2}
    swapped = swap_key_values(dict_)

    assert dict_ == {"a": 1, "b": 1, "c": 1, "d": 2}, "original dict must be unchanged"
    assert swapped == {1: "c", 2: "d"}


def test_swap_key_values_with_list_values():
    dict_ = {"a": ["patate"], "b": ["poil"], "c": "roger"}

    with pytest.raises(TypeError):
        swapped = swap_key_values(dict_)

    assert dict_ == {
        "a": ["patate"],
        "b": ["poil"],
        "c": "roger",
    }, "original dict must be unchanged"


def test_remap():
    dict_ = {"a": 1, "b": 2, "c": 3}
    remapped = remap(dict_, {"a": "first", "b": "second", "c": "patate"})

    assert dict_ == {"a": 1, "b": 2, "c": 3}, "original dict must be unchanged"
    assert remapped == {"first": 1, "second": 2, "patate": 3}


def test_remap_edge_cases():
    dict_ = {"a": 1, "b": 2, "c": 3}
    first_remap = {"a": "painkiller"}
    second_remap = {"jean-roger": "poil"}

    first_remapped = remap(dict_, first_remap)
    assert first_remapped == {"painkiller": 1, "b": 2, "c": 3}

    second_remap = remap(dict_, second_remap)
    assert second_remap == {"a": 1, "b": 2, "c": 3}

    assert dict_ == {"a": 1, "b": 2, "c": 3}, "original dict must be unchanged"


def test_get_first_non_null():
    dict_ = {"a": None, "b": None, "c": "patate", "d": "roger"}

    assert (
        get_first_non_null(dict_, "a", "b", "c", "d", default="painkiller")
        == "patate"
    )
    assert (
        get_first_non_null(dict_, "a", "b", default="judas priest")
        == "judas priest"
    )
    assert (
        get_first_non_null(
            dict_, "poil", "légume", default="jean pierre ferland"
        )
        == "jean pierre ferland"
    )

    assert dict_ == {
        "a": None,
        "b": None,
        "c": "patate",
        "d": "roger",
    }, "original dict must be unchanged"
