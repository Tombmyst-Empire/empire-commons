from typing import Any

from empire_commons.list_util import try_get
from empire_commons.types_ import NULL


def dummy_that_returns_none(*args, **kwargs):
    """
    A function that does nothing else than returning None.
    """
    return None


def dummy_that_does_nothing(*args, **kwargs):
    """
    A function that does nothing.
    """
    pass


def dummy_that_returns_first_arg(*args, **kwargs):
    """
    A function that returns the first argument passed to it, whether
    a star arg or a kwarg.
    """
    if (arg := try_get(list(args), 0, NULL)) is not NULL:
        return arg
    elif kwargs:
        kwarg = kwargs.get(list(kwargs.keys())[0], NULL)
        if kwarg is not NULL:
            return kwarg
    else:
        return None


def get_(value: Any) -> Any:
    """
    Returns *value*. Usefull in DefferedCalls and chaining of functions
    """
    return value