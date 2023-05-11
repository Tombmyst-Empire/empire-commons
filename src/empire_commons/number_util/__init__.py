from contextlib import suppress
import re

from empire_commons.commons.core.core import (
    number_util_to_int
)

_REGROUP_FLOAT_REGEX = re.compile(r"([\d]*[.]?[\d]+)")


def to_int(
    s: str,
    default: int = 0, *,
    strip_non_numeric_chars: bool = False
) -> int:
    """
    Tries to cast an integer-like string to an integer by removing, if *strip_non_numeric_chars* is True,
    characters that are not numbers nor constituents of a number (does not discriminate integers from floats).

    If the method is unable to do the operation, it returns *default*.
    """
    return number_util_to_int(s, default, strip_non_numeric_chars)


def to_float(
    s: str,
    default: float = 0.0,
    *,
    strip_non_numeric_chars: bool = False
) -> float:
    if strip_non_numeric_chars:
        s = "".join(_REGROUP_FLOAT_REGEX.findall(s))

    with suppress(ValueError):
        return float(s)

    return default
