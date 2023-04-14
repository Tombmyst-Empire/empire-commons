import re
from contextlib import suppress

_REGROUP_NUMBER_REGEX = re.compile(r"([\d]*[.]?[\d]+)")


def cast_string_to_float(
        s: str,
        default: float = 0.0,
        *,
        strip_non_numeric_chars: bool = False
) -> float:
    return try_cast_float(s, default, strip_non_numeric_chars=strip_non_numeric_chars)

def try_cast_float(
        s: str,
        default: float = 0.0,
        *,
        strip_non_numeric_chars: bool = False
) -> float:
    if strip_non_numeric_chars:
        s = "".join(_REGROUP_NUMBER_REGEX.findall(s))

    with suppress(ValueError):
        return float(s)

    return default
