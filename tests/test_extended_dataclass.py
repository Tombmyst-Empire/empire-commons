from dataclasses import dataclass
from types import MappingProxyType

import pytest
from bidict import bidict
from frozendict import frozendict

from empire_commons.commons.extended_dataclass import ExtendedDataclass, to_json
from empire_commons.commons import list_util


@dataclass
class NormalDataclass(ExtendedDataclass):
    roger: str
    raoul: int


@dataclass(frozen=True, slots=True)
class TheWayDataclassShouldBe(ExtendedDataclass):
    patate: str
    poil: float


def test_extended_dataclass_dunder_contains():
    first = NormalDataclass(roger="gontrand", raoul=123)
    second = TheWayDataclassShouldBe(
        patate="the thing that should not be", poil=3.141592
    )

    assert "roger" in first
    assert "raoul" in first
    assert "patate" in second
    assert "poil" in second


def test_extended_dataclass_keys():
    first = NormalDataclass(roger="gontrand", raoul=123)
    second = TheWayDataclassShouldBe(
        patate="the thing that should not be", poil=3.141592
    )

    assert isinstance(first.keys(), tuple)
    assert isinstance(first.keys()[0], str)

    assert first.keys() == ("roger", "raoul")
    assert second.keys() == ("patate", "poil")


def test_extended_dataclass_values():
    first = NormalDataclass(roger="gontrand", raoul=123)
    second = TheWayDataclassShouldBe(
        patate="the thing that should not be", poil=3.141592
    )

    assert isinstance(first.values(), tuple)
    assert first.values() == ("gontrand", 123)
    assert second.values() == ("the thing that should not be", 3.141592)


def test_extended_dataclass_items():
    first = NormalDataclass(roger="gontrand", raoul=123)
    second = TheWayDataclassShouldBe(
        patate="the thing that should not be", poil=3.141592
    )

    assert first.items() == {"roger": "gontrand", "raoul": 123}
    assert isinstance(first.items(), MappingProxyType)
    with pytest.raises(KeyError):
        assert (
            first.items()["julien"] == "plante"
        ), "items should return a MappingProxy and is immutable"

    assert second.items() == {
        "patate": "the thing that should not be",
        "poil": 3.141592,
    }


def test_extended_dataclass_dunder_getitem():
    first = NormalDataclass(roger="gontrand", raoul=123)
    second = TheWayDataclassShouldBe(
        patate="the thing that should not be", poil=3.141592
    )

    assert first["roger"] == "gontrand"
    assert first["raoul"] == 123

    assert second["patate"] == "the thing that should not be"
    assert second["poil"] == 3.141592


def test_to_json():
    @dataclass
    class TestClass:
        a_str: str
        an_int: int
        a_list: list
        a_tuple: tuple
        a_dict: dict
        a_frozendict: frozendict
        a_set: set
        a_frozenset: frozenset
        a_bidict: bidict

    tc = TestClass(
        'patate',
        123,
        ['a', 'b', {'rogers': 'gontrand'}],
        ([1, 2], [3, 4]),
        {'germaine': {'gontrand', 'richard'}, 'julien': 'plante'},
        frozendict({'natacha': ('gontrand', 'plante')}),
        {'germaine', 'julien'},
        frozenset({'natacha', 'julien'}),
        bidict({'henri': 'paulin', 'jacqueline': 'gunther'})
    )

    j = to_json(tc)

    assert j['a_str'] == 'patate'
    assert j['an_int'] == 123
    assert j['a_list'] == ['a', 'b', {'rogers': 'gontrand'}]
    assert j['a_tuple'] == [[1, 2], [3, 4]]
    assert list_util.equals(j['a_dict']['germaine'], ['gontrand', 'richard'])
    assert j['a_dict']['julien'] == 'plante'
    assert list_util.equals(j['a_frozendict']['natacha'], ['gontrand', 'plante'])
    assert list_util.equals(j['a_set'], ['germaine', 'julien'])
    assert list_util.equals(j['a_frozenset'], ['natacha', 'julien'])
    assert j['a_bidict'] == {'henri': 'paulin', 'jacqueline': 'gunther'}
