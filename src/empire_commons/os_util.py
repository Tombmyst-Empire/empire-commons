import platform
try:
    from enum import StrEnum
except ImportError:
    from enum import Enum as StrEnum


__all__ = [
    'OSNames',
    'os_name'
]


class OSNames(StrEnum):
    WINDOWS = 'windows'
    LINUX = 'linux'
    MAC = 'darwin'
    JAVA = 'java'
    UNKNOWN = ''


def os_name() -> OSNames:
    return OSNames(platform.system().lower())


def os_name_OLD() -> str:
    return platform.system().lower()
    

___WINDOWS___: Final[bool] = True if os_name() == 'windows' else False
___MAC___: Final[bool] = True if os_name() == 'mac' else False
___LINUX___: Final[bool] = True if os_name() == 'linux' else False
