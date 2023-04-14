"""
Error handling module.
"""

import logging
from enum import Enum, auto
from functools import wraps
from typing import Optional, Type, Any


class OnError(Enum):
    """
    Enum that defines behaviors when errors occur
    """
    RAISE = auto()
    LOG = auto()
    IGNORE = auto()


def handle_error(error: Exception, behavior: OnError, *, logger: Optional[logging.Logger] = None, message: str = None):
    """
    Error handling function.
    :param error: The exception instance
    :param behavior: The behavior to adopt.
    :param logger: An instance of logger. If not provided uses the default logger
    :param message: A custom message to log
    """
    if behavior == OnError.LOG:
        logger = logger or logging.getLogger()
        logger.error(f'Error {format_error(error)}: {message}' if message else f'An error occurred: {format_error(error)}', stacklevel=2)
    elif behavior == OnError.RAISE:
        raise error


def format_error(error: Exception) -> str:
    return f'{type(error).__name__} -> "{error}"'


def catch(
    default_on_error_behavior: OnError = OnError.LOG,
    logger: logging.Logger | None = None,
    error_message: str | None = None,
    errors_to_catch: Type[Exception] | tuple[Type[Exception]] = Exception,
    value_to_return_on_error: Any = None
):
    """
    A decorator that handles possible errors of a function. The wrapped function automatically
    handles the parameter *on_error*, which can change at runtime the *default_on_error_behavior*,
    defined at compile-time

    :param default_on_error_behavior: Default on error behavior
    :param logger: Logger to use
    :param error_message: Error message to print along the error
    :param errors_to_catch: Error(s) to catch
    :param value_to_return_on_error: Value to return in case the function raises an error.
    """
    def _catch(func):
        @wraps(func)
        def wrapper(*args, on_error: OnError = None, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors_to_catch as error:
                handle_error(error, on_error or default_on_error_behavior, logger=logger, message=error_message)
                return value_to_return_on_error
        return wrapper
    return _catch


if __name__ == '__main__':
    @catch(value_to_return_on_error='Patate')
    def a():
        raise TypeError('Roger')

    print(a())
