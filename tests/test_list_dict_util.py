from copy import deepcopy
from empire.commons import list_dict_util, list_util


def test_only_keep_these_root_keys():
    l = [{'a': 1, 'b': 2, 'c': 5}, {'a': 3, 'b': 4, 'c': 10}, {'a': 5, 'b': 6, 'c': 15}]
    l_safe = deepcopy(l)

    assert list_dict_util.keep_root_keys(l, 'a', 'b') == [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
    assert l == l_safe


def test_create_dict_from_list():
    l = [{'a': 1, 'b': 2, 'c': 5}, {'a': 3, 'b': 4, 'c': 10}, {'a': 5, 'b': 6, 'c': 15}]
    l_safe = deepcopy(l)

    assert list_dict_util.create_dict_from_list_of_dicts(l, 'a') == {1: {'a': 1, 'b': 2, 'c': 5}, 3: {'a': 3, 'b': 4, 'c': 10}, 5: {'a': 5, 'b': 6, 'c': 15}}
    assert l == l_safe


def test_exists_within_a_list_of_dicts():
    l = [{"a": 1}, {"a": 2}, {"a": 3, "b": True}]

    assert list_dict_util.exists_within_a_list_of_dicts(l, key_to_match="b")
    assert not list_dict_util.exists_within_a_list_of_dicts(l, key_to_match="c")
    assert list_dict_util.exists_within_a_list_of_dicts(l, key_to_match="a", value_to_match=2)
    assert not list_dict_util.exists_within_a_list_of_dicts(
        l, key_to_match="a", value_to_match=49
    )
    assert list_util.equals(
        l, [{"a": 1}, {"a": 2}, {"a": 3, "b": True}]
    ), "original list must not change"


def test_get_within_a_list_of_dicts():
    l = [{"a": 1}, {"a": 2}, {"a": 3, "b": True}]

    assert list_dict_util.get_within_a_list_of_dicts(l, dictionary_key="b") == {
        "a": 3,
        "b": True,
    }
    assert list_dict_util.get_within_a_list_of_dicts(l, dictionary_key="c") == {}
    assert list_dict_util.get_within_a_list_of_dicts(
        l, dictionary_key="a", dictionary_value=1
    ) == {"a": 1}
    assert (
        list_dict_util.get_within_a_list_of_dicts(l, dictionary_key="a", dictionary_value=123)
        == {}
    )
    assert list_util.equals(
        l, [{"a": 1}, {"a": 2}, {"a": 3, "b": True}]
    ), "original list must not change"
