from time import time
from typing import Final


class _State:
    __run_once: bool = False

    start_time: float = 0.0

    @staticmethod
    def run():
        _State.start_time = time()
        _State.__run_once = True


class Level:
    __slots__ = (
        'weight',
        'name'
    )

    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name

    def __eq__(self, other) -> bool:
        return isinstance(other)


class Levels:
    ALL: Final[Level] = Level(0, 'ALL')
    TRACE: Final[Level] = Level(10, 'TRACE')
    DEBUG: Final[Level] = Level(20, 'DEBUG')
    SUCCESS: Final[Level] = Level(30, 'SUCCESS')
    INFO: Final[Level] = Level(40, 'INFO')
    WARN: Final[Level] = Level(50, 'WARN')
    ERROR: Final[Level] = Level(60, 'ERROR')
    SEVERE: Final[Level] = Level(70, 'SEVERE')
    FATAL = Final[Level] = Level(80, 'FATAL')
