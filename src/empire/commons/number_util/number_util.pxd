cpdef int cast_string_to_int(
        str s,
        int default = *,
        bint strip_non_numeric_chars = *
)
cpdef int try_cast_int(str s, int default = *)

cpdef int clamp_int(int number, int minimum, int maximum)
cpdef float clamp_float(float number, float minimum, float maximum)
