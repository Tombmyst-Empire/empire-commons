from empire_commons import number_util


def test_cast_string_to_int():
    assert number_util.to_int("54d9344.45345.") == 0
    assert (
        number_util.to_int("54d9344.45345.", strip_non_numeric_chars=True)
        == 0
    )
    assert number_util.to_int("123b") == 0
    assert number_util.to_int("123b", strip_non_numeric_chars=True) == 123
    assert number_util.to_int("456") == 456
    assert number_util.to_int("456", strip_non_numeric_chars=True) == 456


def test_cast_string_to_float():
    assert number_util.to_float("54d9344.45345.") == 0.0
    assert (
        number_util.to_float("54d9344.45345.", strip_non_numeric_chars=True)
        == 549344.45345
    )
    assert number_util.to_float("3.2.1") == 0.0
    assert number_util.to_float("3.2.1", strip_non_numeric_chars=True) == 0.0
    assert number_util.to_float("3.14") == 3.14
    assert number_util.to_float("3.14", strip_non_numeric_chars=True) == 3.14
    assert number_util.to_float("123") == 123.0
    assert number_util.to_float("123", strip_non_numeric_chars=True) == 123.0
