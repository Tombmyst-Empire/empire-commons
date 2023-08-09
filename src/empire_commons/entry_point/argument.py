from dataclasses import dataclass, field
from enum import StrEnum
from typing import Literal, Any, Sequence, Optional


class ArgumentAction(StrEnum):
    """
    https://docs.python.org/3/library/argparse.html#action
    """
    STORE = 'store'
    STORE_CONST = 'store_const'
    STORE_TRUE = 'store_true'
    STORE_FALSE = 'store_false'
    APPEND = 'append'
    EXTEND = 'extend'
    APPEND_CONST = 'append_const'
    COUNT = 'count'
    HELP = 'help'
    VERSION = 'version'


@dataclass(frozen=True, slots=True, init=False)
class Argument:
    """
    https://docs.python.org/3/library/argparse.html
    """
    name_or_flags: tuple[str]
    action: ArgumentAction = ArgumentAction.STORE
    nargs: Optional[Literal['?', '*', '+'] | int] = None
    const: Any = None
    default: Any = None
    type: type = str
    choices: Optional[Sequence[str]] = None
    required: bool = False
    help: Optional[str] = None
    metavar: Optional[str] = None
    dest: Optional[str] = None
