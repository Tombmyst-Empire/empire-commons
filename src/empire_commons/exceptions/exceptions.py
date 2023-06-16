"""
Module that contains Empire exceptions
"""
from typing import Any


__all__ = [
    'EmpireException',
    'HTTPException',
    'ProgrammingException',
    'UnknownValueException',
    'UnexpectedCoreException',
    'UnexpectedTypeException',
    'UnexpectedException'
]


class EmpireException(Exception):
    """
    Mother of all Empire exceptions.
    """

    def __init__(self, message: str):
        super().__init__(message)


class HTTPException(Exception):
    def __init__(self, result: 'HTTPResult'):
        super().__init__(f'Query failed with code {result.status_code}: {result.text[:1000]}')


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
