import math


cdef class Vec2D:
    def __cinit__(self, double x, double y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vec2D(%f, %f)" % (self.x, self.y)

    cdef inline bint is_nan(self):
        return self.x == self.y == math.nan
