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
