cdef class Vec2D:
    cdef public double x
    cdef public double y

    cdef inline bint is_nan(self)