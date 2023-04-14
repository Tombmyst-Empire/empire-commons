import re
from contextlib import suppress

cdef REGROUP_NUMBER_REGEX = re.compile(r"([\d]*[.]?[\d]+)")


cpdef int cast_string_to_int(
        str s,
        int default = 0,
        bint strip_non_numeric_chars = False
):
    if strip_non_numeric_chars:
        s = "".join(REGROUP_NUMBER_REGEX.findall(s))

    with suppress(Exception):
        return int(s)

    return default


cpdef int try_cast_int(str s, int default = 0):
    with suppress(Exception):
        return int(s)

    return default

cpdef int clamp_int(int number, int minimum, int maximum):
    if number < minimum:
        return minimum
    elif number > maximum:
        return maximum
    else:
        return number

cpdef float clamp_float(float number, float minimum, float maximum):
    if number < minimum:
        return minimum
    elif number > maximum:
        return maximum
    else:
        return number
