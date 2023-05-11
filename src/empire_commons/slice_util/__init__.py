from empire_commons.commons.core.core import (
    slice_util_contains,
    slice_util_number_is_in,
    slice_util_get_slice_coverage,
    slice_util_get_slice_with_most_coverage, Vec2D
)


def number_is_in(
    slice_obj: slice,
    number: int,
    *,
    inclusive: bool = False
) -> bool:
    """
    Returns True if *number* is contained within *slice_obj*.
    """
    return slice_util_number_is_in(slice_obj, number, inclusive)


def contains(
    containing_slice: slice,
    slice_to_be_contained: slice
) -> bool:
    """
    Returns True if *slice_to_be_contained* is contained within *containing_slice*.
    """
    return slice_util_contains(containing_slice, slice_to_be_contained)


def get_slice_with_most_coverage(
    reference_slice: slice,
    slice_a: slice,
    slice_b: slice
) -> slice:
    """
    Returns the slice object with the most coverage.

    Example:

    You have 2 slices: (0, 10) and (10, 20). Reference slice is (8, 18), then
    the slice with most coverage would be the second.
    """
    return slice_util_get_slice_with_most_coverage(reference_slice, slice_a, slice_b)


def get_slice_coverage(
    reference_slice: slice,
    slice_a: slice,
    slice_b: slice
) -> Vec2D:
    """
    Computes the coverage score for *slice_a* and *slice_b* on *reference_slice*.

    Returns a Vec2D where X is the coverage score for *slice_a* and Y is the coverage
    score for *slice_b*.
    """
    return slice_util_get_slice_coverage(reference_slice, slice_a, slice_b)


def from_string(
        s: str
) -> slice:
    """
    Parses string *s* into a slice object. If the stringified slice does not
    provide an ending bound, *max stop* should be the length of the object
    to slice.
    """
    s = s.replace('[', '').replace(']', '')
    try:
        return slice(*map(lambda x: int(x.strip()) if x.strip() else None, s.split(':')))
    except TypeError:
        return slice(None, None, None)
