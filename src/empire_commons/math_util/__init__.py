from empire_commons.commons.types_ import NumberType

from empire_commons.commons.core.core import (
    math_util_avg,
    math_util_clamp_int,
    math_util_clamp_float
)


def avg(*data: NumberType) -> float:
    return math_util_avg(*data)


def clamp_int(number: int, minimum: int, maximum: int) -> int:
    """
    Clamps integer *number* between *minimum* and *maximum*
    """
    return math_util_clamp_int(number, minimum, maximum)


def clamp_float(number: float, minimum: float, maximum: float) -> float:
    """
    Clamps float *number* between *minimum* and *maximum*
    """
    return math_util_clamp_float(number, minimum, maximum)
