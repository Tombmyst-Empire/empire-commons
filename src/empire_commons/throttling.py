"""
Module containing throttling function and decorator
"""
from enum import IntEnum
from functools import wraps
from time import sleep, time
from typing import Any, Callable

from empire_commons.commons.types_ import NumberType


class Per(IntEnum):
    """
    Simple enum containing pre-calculated seconds
    """

    DAY = 86_400
    HOUR = 3600
    MINUTE = 60
    SECOND = 1


def throttler(func: Callable, at: NumberType, per: Per) -> Any:
    """
    Throttles a function to *at* calls per *per*.

    The difference between this function and the decorator is that parameters *at* and *per* can be determined at runtime.

    Example call: ::

        def b(i):
            print(f'B {i}', time())

        bb = throttler(b, 15, Per.MINUTE)

        for i in range(10):
            bb(i)

    Prints: ::

        B 0 1653595771.0122366
        B 1 1653595775.0160131
        B 2 1653595779.0200346
        B 3 1653595783.0239923
        B 4 1653595787.0280106
        B 5 1653595791.0320122
        B 6 1653595795.036024
        B 7 1653595799.0400279
        B 8 1653595803.0440001
        B 9 1653595807.0480952
    """
    delay_in_seconds: float = per / at
    last_execution: float = time() - delay_in_seconds

    @wraps(func)
    def _throttler(*args, **kwargs):
        nonlocal last_execution

        while True:
            current_time: float = time()
            if current_time - last_execution > delay_in_seconds:
                last_execution = time()
                return func(*args, **kwargs)
            else:
                sleep(delay_in_seconds)

    return _throttler


def throttler_decorator(
    at: NumberType, per: int
):  # Configuration must be defined at compile time
    delay_in_seconds: float = per / at
    last_execution: float = time() - delay_in_seconds

    def _throttled(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_execution
            while True:
                current_time: float = time()
                if current_time - last_execution > delay_in_seconds:
                    last_execution = time()
                    return func(*args, **kwargs)
                else:
                    sleep(delay_in_seconds)

        return wrapper

    return _throttled


if __name__ == "__main__":

    @throttler_decorator(0.5, Per.SECOND)
    def a(i):
        print(f"A {i}", time())

    for i in range(10):
        pass  # a(i)

    def b(i):
        print(f"B {i}", time())

    bb = throttler(b, 15, Per.MINUTE)

    for i in range(10):
        bb(i)
