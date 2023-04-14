from typing import Optional

from empire.commons.vector.vec2d import Vec2D


def slice_is_in(
        slice_obj: slice,
        number: int,
        inclusive: bool = False
) -> bool:
    """
    Returns True if *number* is contained within *slice_obj*.
    """

def slice_contains_slice(
        containing_slice: slice,
        slice_to_be_contained: slice
) -> bool:
    """
    Returns True if *slice_to_be_contained* is contained within *containing_slice*.
    """

def get_slice_object_with_most_coverage(
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
