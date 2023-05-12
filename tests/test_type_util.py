from frozendict import frozendict

from empire_commons import type_util


def test_is_not_empty():
    assert type_util.is_empty('patate') is False
    assert type_util.is_empty('') is True
    assert type_util.is_empty(str()) is True

    assert type_util.is_empty({'patate'}) is False
    assert type_util.is_empty({'patate': 'roger'}) is False
    assert type_util.is_empty(frozendict({'patate': 'roger'})) is False
    assert type_util.is_empty(frozenset({'patate'})) is False
    assert type_util.is_empty({}) is True
    assert type_util.is_empty(dict()) is True
    assert type_util.is_empty(frozendict()) is True
    assert type_util.is_empty(frozenset()) is True
    assert type_util.is_empty(set()) is True

    assert type_util.is_empty(('patate',)) is False
    assert type_util.is_empty(tuple()) is True
    assert type_util.is_empty(()) is True

    assert type_util.is_empty(['patate']) is False
    assert type_util.is_empty([]) is True
    assert type_util.is_empty(list()) is True

    assert type_util.is_empty(0) is False


def test_is_mutable():
    assert type_util.is_mutable([]) is True
    assert type_util.is_mutable({}) is True
    assert type_util.is_mutable(set()) is True
    assert type_util.is_mutable(frozenset()) is False
    assert type_util.is_mutable(str()) is False
    assert type_util.is_mutable(int()) is False

