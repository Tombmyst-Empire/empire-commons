"""
Error handling module.
"""
import logging
from enum import Enum, auto
from functools import wraps
from typing import Optional, Type, Any, Callable, Protocol

import ereport


class OnError(Enum):
    """
    Enum that defines behaviors when errors occur
    """
    RAISE = auto()
    LOG = auto()
    IGNORE = auto()


def handle_error(error: Exception, behavior: OnError, *, reporter: Optional[ereport.Reporter] = None, message: str = None):
    """
    Error handling function.
    :param error: The exception instance
    :param behavior: The behavior to adopt.
    :param reporter: An instance of logger. If not provided uses the default logger
    :param message: A custom message to log
    """
    if behavior == OnError.LOG:
        reporter = reporter or ereport.get_or_make_reporter()
        reporter.error(f'Error {format_error(error)}: {message}' if message else f'An error occurred: {format_error(error)}')
    elif behavior == OnError.RAISE:
        raise error


def handle_error2(
        callable_: Callable,
        *args,
        on_error_behavior_: OnError = OnError.RAISE,
        reporter_: ereport.Reporter | None = None,
        message_: str = None,
        **kwargs
) -> Any:
    """
    Error handling function.
    :param callable_: The callable to call. Star args and kw args are passed to it.
    :param on_error_behavior_: The behavior to adopt.
    :param reporter_: An instance of logger. If not provided uses the default logger
    :param message_: A custom message to log
    :returns: The return value of *callable_*
    """
    try:
        return callable_(*args, **kwargs)
    except Exception as error:
        if on_error_behavior_ == OnError.LOG:
            reporter = reporter_ or ereport.get_or_make_reporter()
            reporter.error(f'Error {format_error(error)}: {message_}'
                           if message_ else
                           f'An error occurred in {callable_.__qualname__}: {format_error(error)}',
                           stack_level=1)
        elif on_error_behavior_ == OnError.RAISE:
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
                handle_error(error, on_error or default_on_error_behavior, reporter=logger, message=error_message)
                return value_to_return_on_error
        return wrapper
    return _catch


if __name__ == '__main__':
    @catch(value_to_return_on_error='Patate')
    def a():
        raise TypeError('Roger')

    print(a())
