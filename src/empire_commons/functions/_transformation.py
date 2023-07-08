from typing import Callable


def to_closure(function: Callable, *args, **kwargs) -> Callable:
    """
    Transforms *function* to a closure
    """
    def _closure():
        return function(*args, **kwargs)

    return _closure