import pytest

from empire_commons.tristate import Tristate


def test_tristate_truthy():
    t = Tristate(True)

    if not t:
        pytest.xfail("Should not occur")

    assert t.is_true
    assert t.is_false == t.is_indeterminate is False
    assert int(t) == 1
    assert str(t) == repr(t) == "Tristate(True)"


def test_tristate_falsy():
    t = Tristate(False)

    if t:
        pytest.xfail("Should not occur")

    assert t.is_false
    assert t.is_true == t.is_indeterminate is False
    assert int(t) == 0
    assert str(t) == repr(t) == "Tristate(False)"


def test_tristate_indeterminaty():
    t = Tristate()

    if t:
        pytest.xfail("Should not occur")

    assert t.is_indeterminate
    assert t.is_true == t.is_false is False
    assert int(t) == -1
    assert str(t) == repr(t) == "Tristate(Indeterminate)"


def test_tristate_dunder_eq_ne():
    t_true1 = Tristate(True)
    t_true2 = Tristate(True)

    t_false1 = Tristate(False)
    t_false2 = Tristate(False)

    t_ind1 = Tristate()
    t_ind2 = Tristate()

    assert t_true1 == t_true2
    assert t_false1 == t_false2
    assert t_ind1 == t_ind2

    assert t_true1 != t_false1
    assert t_true1 != t_ind1
    assert t_false1 != t_ind1


def test_tristate_bin_and_truth_table():
    t_true1 = Tristate(True)
    t_true2 = Tristate(True)

    t_false1 = Tristate(False)
    t_false2 = Tristate(False)

    t_ind1 = Tristate()
    t_ind2 = Tristate()

    assert t_true1 & t_true2 == Tristate(True)
    assert t_true1 & t_false1 == Tristate(False)
    assert t_false1 & t_false2 == Tristate(False)
    assert t_true1 & t_ind1 == Tristate()
    assert t_false1 & t_ind1 == Tristate()
    assert t_ind1 & t_ind2 == Tristate()


def test_tristate_bin_or_truth_table():
    t_true1 = Tristate(True)
    t_true2 = Tristate(True)

    t_false1 = Tristate(False)
    t_false2 = Tristate(False)

    t_ind1 = Tristate()
    t_ind2 = Tristate()

    assert t_true1 | t_true2 == Tristate(True)
    assert t_true1 | t_false1 == Tristate(True)
    assert t_false1 | t_false2 == Tristate(False)
    assert t_true1 | t_ind1 == Tristate()
    assert t_false1 | t_ind1 == Tristate()
    assert t_ind1 | t_ind2 == Tristate()


def test_tristate_bin_xor_truth_table():
    t_true1 = Tristate(True)
    t_true2 = Tristate(True)

    t_false1 = Tristate(False)
    t_false2 = Tristate(False)

    t_ind1 = Tristate()
    t_ind2 = Tristate()

    assert t_true1 ^ t_true2 == Tristate(False)
    assert t_true1 ^ t_false1 == Tristate(True)
    assert t_false1 ^ t_false2 == Tristate(False)
    assert t_true1 ^ t_ind1 == Tristate()
    assert t_false1 ^ t_ind1 == Tristate()
    assert t_ind1 ^ t_ind2 == Tristate()
