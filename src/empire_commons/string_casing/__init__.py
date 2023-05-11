from empire_commons.commons.core.core import (
    string_casing_to_camel_case_strip_spaces,
    string_casing_to_pascal_case_strip_spaces,
    string_casing_to_upper_case_with_underscores,
    string_casing_to_camel_case_with_underscores,
    string_casing_to_pascal_case_with_underscores
)


def to_camel_case_strip_spaces(the_string: str) -> str:
    return string_casing_to_camel_case_strip_spaces(the_string)


def to_camel_case_with_underscores(the_string: str) -> str:
    return string_casing_to_camel_case_with_underscores(the_string)


def to_pascal_case_strip_spaces(the_string: str) -> str:
    return to_pascal_case_strip_spaces(the_string)


def to_pascal_case_with_underscores(the_string: str) -> str:
    return string_casing_to_pascal_case_with_underscores(the_string)


def to_upper_case_with_underscores(the_string: str) -> str:
    return string_casing_to_upper_case_with_underscores(the_string)

