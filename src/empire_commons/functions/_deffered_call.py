from typing import Callable, Any


class DefferedCall:
    __slots__ = (
        '_callable',
        '_star_args',
        '_kwargs'
    )

    def __init__(
            self,
            callable_: Callable,
            *args: Any,
            **kwargs: Any
    ):
        self._callable = callable_
        self._star_args = args
        self._kwargs = kwargs

    def __call__(self, *call_args, **call_kwargs) -> Any:
        # TODO: handle TypeError when passing wrong arguments (example, unknown kwarg)
        #   show passed args+kwargs to function, and show function signature
        return self._callable(*(self._star_args + call_args), **(self._kwargs | call_kwargs))

    def __repr__(self) -> str:
        return f'DefferedCall({self._callable}, {self._star_args}, {self._kwargs})'


def coalesce_deffered(*items: DefferedCall) -> Any:
    """
    Returns first non-None value from DefferedCall *items*.

    The difference with *coalesce()* is that *items* callables are called sequentially
    up until a call returns something else than None.
    """
    current_return: Any = None

    for item in items:
        current_return = item()
        if current_return is not None:
            return current_return

    return current_return
