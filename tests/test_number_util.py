from empire.commons.number_util import cast_string_to_float, cast_string_to_int, try_cast_int


def test_cast_string_to_int():
    assert cast_string_to_int("54d9344.45345.") == 0
    assert (
        cast_string_to_int("54d9344.45345.", strip_non_numeric_chars=True)
        == 0
    )
    assert cast_string_to_int("123b") == 0
    assert cast_string_to_int("123b", strip_non_numeric_chars=True) == 123
    assert cast_string_to_int("456") == 456
    assert cast_string_to_int("456", strip_non_numeric_chars=True) == 456


def test_cast_string_to_float():
    assert cast_string_to_float("54d9344.45345.") == 0.0
    assert (
        cast_string_to_float("54d9344.45345.", strip_non_numeric_chars=True)
        == 549344.45345
    )
    assert cast_string_to_float("3.2.1") == 0.0
    assert cast_string_to_float("3.2.1", strip_non_numeric_chars=True) == 0.0
    assert cast_string_to_float("3.14") == 3.14
    assert cast_string_to_float("3.14", strip_non_numeric_chars=True) == 3.14
    assert cast_string_to_float("123") == 123.0
    assert cast_string_to_float("123", strip_non_numeric_chars=True) == 123.0


def test_try_cast_int():
    assert try_cast_int("123", 111) == 123
    assert try_cast_int("roger", 111) == 111
