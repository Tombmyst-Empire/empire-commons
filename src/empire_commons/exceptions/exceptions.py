"""
Module that contains Empire exceptions
"""
from typing import Any


__all__ = [
    'EmpireException',
    'HTTPException',
    'InvalidValueException',
    'ProgrammingException',
    'UnknownValueException',
    'UnexpectedCoreException',
    'UnexpectedTypeException',
    'UnexpectedException'
]

from empire_commons.types_ import NULL


class EmpireException(Exception):
    """
    Mother of all Empire exceptions.
    """

    def __init__(self, message: str):
        super().__init__(message)


class HTTPException(Exception):
    def __init__(self, result: 'HTTPResult'):
        super().__init__(f'Query failed with code {result.status_code}: {result.text[:1000]}')


class InvalidValueException(Exception):
    """
    - What: example, the variable name
    - is_: the actual value
    - should_be: the value it should be
    - should_be_info: a string explaining what the value can be (example, "between 0 and 1")
    """
    def __init__(self, what: str, is_: Any, should_be_info: str = NULL, should_be: Any = NULL):
        effective_should_be: str = should_be if should_be != NULL else f'"{should_be_info}"'

        super().__init__(f'Invalid value for "{what}": Should be {effective_should_be} (type: {type(should_be).__name__}), not: {is_} (type: {type(is_).__name__})')


class ProgrammingException(Exception):
    """
    An error because of you.
    """

    def __init__(self, message: str):
        super().__init__(f"Programming error: {message}")


class UnknownValueException(Exception):
    """
    An error caused by a value that is unknown by the code, example, when going through the possible values of an enum, but having
    a value that is not contained in this enum.
    """
    def __init__(self, value: Any):
        super().__init__(f'Unknown value: {value}')


class UnexpectedTypeException(EmpireException):
    def __init__(self, for_what: str, expected: str | type, actual: str | type):
        super().__init__(f'Unexpected type for: "{for_what}". Expecting: "{expected}", got: "{actual}"')


class UnexpectedCoreException(EmpireException):
    def __init__(self, message: str):
        super().__init__(f'Unexpected Core Error: {message}')
        

class UnexpectedException(EmpireException):
    def __init__(self, message: str):
        super().__init__(f'Unexpected state: {message}')

