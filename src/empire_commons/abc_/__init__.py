"""
Mainly this module is to facade Python's ABC deprecation of
abstractstaticmethod and abstractclassmethod, that
apparently have no particular reasons of being deprecated.
"""
from __future__ import annotations
from abc import abstractmethod, ABC, ABCMeta, abstractproperty


__all__ = [
    'abstractmethod',
    'ABC',
    'ABCMeta',
    'abstractproperty',
    'abstractclassmethod',
    'abstractstaticmethod'
]


class abstractclassmethod(classmethod):
    """A decorator indicating abstract classmethods."""

    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)


class abstractstaticmethod(staticmethod):
    """A decorator indicating abstract staticmethods."""

    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super().__init__(callable)
