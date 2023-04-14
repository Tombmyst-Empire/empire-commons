from typing import Optional

from empire.commons.slice_util.slice_util import (
    slice_contains_slice,
    slice_is_in,
    get_slice_coverage,
    get_slice_object_with_most_coverage,
)


def slice_from_string(
        s: str
) -> Optional[slice]:
    """
    Parses string *s* into a slice object. If the stringified slice does not
    provide an ending bound, *max stop* should be the length of the object
    to slice.
    """
    s = s.replace('[', '').replace(']', '')
    return slice(*map(lambda x: int(x.strip()) if x.strip() else None, s.split(':')))
