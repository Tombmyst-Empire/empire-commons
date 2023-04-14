"""
Module containing utility functions for stdout
"""

from contextlib import redirect_stdout
from io import StringIO
from typing import Callable


class _NullIO(StringIO):
    def write(self, __s: str) -> int:  # pylint: disable=missing-function-docstring
        pass


def mute_stdout(func: Callable):
    """
    Mutes out-of-control annoying leftover prints() that are outside of your reach!
    :param func: The function that speaks too much
    """

    def _inner(*args, **kwargs):
        with redirect_stdout(_NullIO()):
            return func(*args, **kwargs)

    return _inner
