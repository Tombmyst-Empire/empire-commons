import platform
from enum import StrEnum


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
