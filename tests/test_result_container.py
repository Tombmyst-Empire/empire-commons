import pytest

from empire.commons.exceptions import ProgrammingException
from empire.commons.result_container import ResultContainer


def test_result_container_immutability():
    rc = ResultContainer([1, 2, 3])

    assert rc.value == [1, 2, 3]
    l = rc.value
    l.append(4)
    assert rc.value == [1, 2, 3]


def test_result_container_dunder_bool():
    rc_ok = ResultContainer("patate", ok=True)
    rc_not_ok = ResultContainer("patate", ok=False)

    if not rc_ok:
        pytest.xfail("Should not occur")

    if rc_not_ok:
        pytest.xfail("Should not occur")


def test_result_container_dunder_len():
    rc_with_len = ResultContainer([1, 2, 3])
    rc_without_len = ResultContainer(123)

    assert len(rc_with_len) == 3

    with pytest.raises(ProgrammingException):
        len(rc_without_len)


def test_result_container_dunder_contains():
    rc_with_contains = ResultContainer("patate")
    rc_without_contains = ResultContainer(345)

    assert "ta" in rc_with_contains
    with pytest.raises(ProgrammingException):
        "jean guy roger" in rc_without_contains
