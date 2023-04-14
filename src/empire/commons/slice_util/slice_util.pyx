import math

from empire.commons.vector.vec2d cimport Vec2D



cpdef bint slice_is_in(
        slice slice_obj,
        int number,
        bint inclusive = False
):
    if slice_obj is None:
        return False

    cdef slice_copy

    if slice_obj.start < 0:
        slice_copy = slice(None, slice_obj.stop)
    elif slice_obj.stop < 0:
        slice_copy = slice(slice_obj.start, None)
    else:
        slice_copy = slice_obj

    if None not in [slice_copy.start, slice_copy.stop]:
        if inclusive:
            return slice_copy.start <= number <= slice_copy.stop
        else:
            return slice_copy.start <= number < slice_copy.stop
    elif slice_copy.start is slice_copy.stop is None:
        return True
    elif slice_copy.start is None:
        if inclusive:
            return number <= slice_copy.stop
        else:
            return number < slice_copy.stop
    elif slice_copy.stop is None:
        return slice_copy.start <= number

    return False


cpdef bint slice_contains_slice(
        slice containing_slice,
        slice slice_to_be_contained
):
    return (
        slice_to_be_contained.start >= containing_slice.start and
        slice_to_be_contained.stop < containing_slice.stop
    )


cpdef slice get_slice_object_with_most_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
):
    cdef Vec2D coverage = get_slice_coverage(reference_slice, slice_a, slice_b)

    if coverage.is_nan():
        return None
    elif coverage.y == math.nan or coverage.x >= coverage.y:
        return slice_a

    return slice_b


cpdef Vec2D get_slice_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
):
    cdef int value_a = slice_a.stop
    cdef int value_b = slice_b.start
    cdef int distance_a
    cdef int distance_b
    cdef int total_distance


    if value_a is value_b is None:
        return Vec2D(math.nan, math.nan)
    elif value_a is None or reference_slice.start is None:
        return Vec2D(100.0, 0.0)
    elif value_b is None:
        return Vec2D(0.0, 100.0)
    else:
        distance_a = abs(abs(value_a) - reference_slice.start)
        distance_b = abs(abs(value_b) - (reference_slice.stop or 0))
        total_distance = distance_a + distance_b
        return Vec2D(
            distance_a * 100 / total_distance,
            distance_b * 100 / total_distance
        )
