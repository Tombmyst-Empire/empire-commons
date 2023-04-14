from empire.commons.vector.vec2d cimport Vec2D


cpdef bint slice_is_in(
        slice slice_obj,
        int number,
        bint inclusive = *
)

cpdef bint slice_contains_slice(
        slice containing_slice,
        slice slice_to_be_contained
)

cpdef slice get_slice_object_with_most_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
)

cpdef Vec2D get_slice_coverage(
        slice reference_slice,
        slice slice_a,
        slice slice_b
)
