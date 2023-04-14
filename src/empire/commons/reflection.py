from typing import Any


def get_type_name(*, instance: Any = None, type_: type = None) -> str:
    if type_:
        return type_.__name__
    else:
        return type(instance).__name__
