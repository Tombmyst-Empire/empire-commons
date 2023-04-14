from __future__ import annotations

from typing import Optional


class Tristate:
    def __init__(self, val: Optional[bool] = None):
        self._val: Optional[bool] = val

    def set_true(self):
        self._val = True

    def set_false(self):
        self._val = False

    def set_indeterminate(self):
        self._val = None

    @property
    def is_true(self) -> bool:
        return self._val is True

    @property
    def is_false(self) -> bool:
        return self._val is False

    @property
    def is_indeterminate(self) -> bool:
        return self._val is None

    def __bool__(self) -> bool:
        return self._val is True

    def __and__(self, other: bool | None | Tristate) -> Tristate:
        if isinstance(other, bool):
            return Tristate(self._val & other)
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            return Tristate()
        elif isinstance(other, Tristate):
            return Tristate(self._val & other._val)
        else:
            raise TypeError("Unsupported type: " + str(type(other)))

    def __eq__(self, other: bool | None | Tristate) -> bool:
        if isinstance(other, Tristate):
            return self._val == other._val
        else:
            return self._val == other

    def __ne__(self, other) -> bool:
        return not (self == other)

    def __hash__(self):
        return hash((self._val, id(self)))

    def __iand__(self, other: bool | Tristate) -> Tristate:
        if isinstance(other, bool):
            self._val &= other
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            self._val = None
        elif isinstance(other, Tristate):
            self._val &= other._val
        else:
            raise TypeError("Unsupported type: " + str(type(other)))
        return self

    def __int__(self) -> int:
        if self._val is True:
            return 1
        elif self._val is False:
            return 0
        else:
            return -1

    def __invert__(self):
        if self._val is not None:
            self._val = ~self._val

    def __ior__(self, other: bool | Tristate) -> Tristate:
        if isinstance(other, bool):
            self._val |= other
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            self._val = None
        elif isinstance(other, Tristate):
            self._val |= other._val
        else:
            raise TypeError("Unsupported type: " + str(type(other)))
        return self

    def __ixor__(self, other: bool | Tristate) -> Tristate:
        if isinstance(other, bool):
            self._val ^= other
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            self._val = None
        elif isinstance(other, Tristate):
            self._val ^= other._val
        else:
            raise TypeError("Unsupported type: " + str(type(other)))
        return self

    def __or__(self, other: bool | None | Tristate) -> Tristate:
        if isinstance(other, bool):
            return Tristate(self._val | other)
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            return Tristate()
        elif isinstance(other, Tristate):
            return Tristate(self._val | other._val)
        else:
            raise TypeError("Unsupported type: " + str(type(other)))

    def __repr__(self) -> str:
        if self._val is True:
            return "Tristate(True)"
        elif self._val is False:
            return "Tristate(False)"
        else:
            return "Tristate(Indeterminate)"

    def __str__(self) -> str:
        if self._val is True:
            return "Tristate(True)"
        elif self._val is False:
            return "Tristate(False)"
        else:
            return "Tristate(Indeterminate)"

    def __xor__(self, other: bool | None | Tristate) -> Tristate:
        if isinstance(other, bool):
            return Tristate(self._val ^ other)
        elif (isinstance(other, Tristate) and other._val is None) or other is None:
            return Tristate()
        elif isinstance(other, Tristate):
            return Tristate(self._val ^ other._val)
        else:
            raise TypeError("Unsupported type: " + str(type(other)))


if __name__ == "__main__":
    ts = Tristate()
    print(ts & None)
