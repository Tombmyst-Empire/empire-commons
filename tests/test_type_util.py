from frozendict import frozendict

from empire.commons.type_util import TypeUtil


def test_is_not_empty():
    assert TypeUtil.is_empty('patate') is False
    assert TypeUtil.is_empty('') is True
    assert TypeUtil.is_empty(str()) is True

    assert TypeUtil.is_empty({'patate'}) is False
    assert TypeUtil.is_empty({'patate': 'roger'}) is False
    assert TypeUtil.is_empty(frozendict({'patate': 'roger'})) is False
    assert TypeUtil.is_empty(frozenset({'patate'})) is False
    assert TypeUtil.is_empty({}) is True
    assert TypeUtil.is_empty(dict()) is True
    assert TypeUtil.is_empty(frozendict()) is True
    assert TypeUtil.is_empty(frozenset()) is True
    assert TypeUtil.is_empty(set()) is True

    assert TypeUtil.is_empty(('patate',)) is False
    assert TypeUtil.is_empty(tuple()) is True
    assert TypeUtil.is_empty(()) is True

    assert TypeUtil.is_empty(['patate']) is False
    assert TypeUtil.is_empty([]) is True
    assert TypeUtil.is_empty(list()) is True

    assert TypeUtil.is_empty(0) is False


def test_is_mutable():
    assert TypeUtil.is_mutable([]) is True
    assert TypeUtil.is_mutable({}) is True
    assert TypeUtil.is_mutable(set()) is True
    assert TypeUtil.is_mutable(frozenset()) is False
    assert TypeUtil.is_mutable(str()) is False
    assert TypeUtil.is_mutable(int()) is False

