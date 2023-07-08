from typing import Any, Callable


def accumulate_callables(initial_value: Any, *callables: Callable) -> Any:
    """
    Takes *initial_value* and passes it to the first callable.

    The result of the first callable is passed to the second, and so on.
    """
    current: Any = initial_value
    for callable_ in callables:
        current = callable_(current)

    return current
