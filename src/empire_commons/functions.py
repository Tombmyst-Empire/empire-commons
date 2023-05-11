from functools import wraps
from typing import Any, Callable

from empire_commons.commons.list_util import try_get
from empire_commons.commons.types_ import NULL


def dummy(*args, **kwargs):
    return None


def dummy_that_returns_first_arg(*args, **kwargs):
    if (arg := try_get(list(args), 0, NULL)) is not NULL:
        return arg
    elif kwargs:
        kwarg = kwargs.get(list(kwargs.keys())[0], NULL)
        if kwarg is not NULL:
            return kwarg
    else:
        return None


def to_closure(function: Callable, *args, **kwargs) -> Callable:
    def _closure():
        return function(*args, **kwargs)

    return _closure


def returns_on_falsy_first_parameter(func):
    """
    Decorator that makes the function returns if the first provided argument of it evaluates to False.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and not args[0]:
            return args[0]

        if not args and kwargs:
            first_key: str = list(kwargs.keys())[0]
            if not kwargs[first_key]:
                return kwargs[first_key]

        return func(*args, **kwargs)

    return wrapper

