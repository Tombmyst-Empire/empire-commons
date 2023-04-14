from copy import deepcopy
from empire.commons.list_dict_util.list_dict_util import only_keep_these_root_keys, create_dict_from_list


def test_only_keep_these_root_keys():
    l = [{'a': 1, 'b': 2, 'c': 5}, {'a': 3, 'b': 4, 'c': 10}, {'a': 5, 'b': 6, 'c': 15}]
    l_safe = deepcopy(l)

    assert only_keep_these_root_keys(l, ['a', 'b']) == [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
    assert l == l_safe


def test_create_dict_from_list():
    l = [{'a': 1, 'b': 2, 'c': 5}, {'a': 3, 'b': 4, 'c': 10}, {'a': 5, 'b': 6, 'c': 15}]
    l_safe = deepcopy(l)

    assert create_dict_from_list(l, 'a') == {1: {'a': 1, 'b': 2, 'c': 5}, 3: {'a': 3, 'b': 4, 'c': 10}, 5: {'a': 5, 'b': 6, 'c': 15}}
    assert l == l_safe
