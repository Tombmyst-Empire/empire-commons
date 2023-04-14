def cast_string_to_int(
        s: str, default: int = 0, *, strip_non_numeric_chars: bool = False
) -> int:
    """
    Tries to cast an integer-like string to an integer by removing, if *strip_non_numeric_chars* is True,
    characters that are not numbers nor constituents of a number (does not discriminate integers from floats).

    If the method is unable to do the operation, it returns *default*.
    """


def cast_string_to_float(
    s: str, default: float = 0.0, *, strip_non_numeric_chars: bool = False
) -> float:
    """
    Tries to cast an integer-like string to an float by removing, if *strip_non_numeric_chars* is True,
    characters that are not numbers nor constituents of a number (does not discriminate integers from floats).

    If the method is unable to do the operation, it returns *default*.
    """


def try_cast_int(s: str, default: int = None) -> int:
    """
    Tries to cast *s* to an integer or returns *default*. The difference with *cast_string_to_int* is that no
    cleansing operation is made prior the conversion.
    """


def clamp_int(number: int, minimum: int, maximum: int) -> int:
    """
    Clamps integer *number* between *minimum* and *maximum*
    """

def clamp_float(number: float, minimum: float, maximum: float) -> float:
    """
    Clamps float *number* between *minimum* and *maximum*
    """
