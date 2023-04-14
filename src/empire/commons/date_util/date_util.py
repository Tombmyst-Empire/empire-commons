import logging
from contextlib import suppress
from datetime import datetime
from dateutil import parser as date_parser


__all__ = [
    'Timestamp',
    'maybe_from_iso',
    'current_timestamp',
    'current_hh_ii_ss',
    'current_dd_mm_yy',
    'current_yy_mm_dd',
    'current_dd_mm_yyyy',
    'current_yyyy_mm_dd',
    'current_dd_mm_yy_hh_ii_ss',
    'current_dd_mm_yyyy_hh_ii_ss',
    'current_yy_mm_dd_hh_ii_ss',
    'current_yyyy_mm_dd_hh_ii_ss'
]

from typing import Any

from empire.commons.on_error import catch, OnError


class Timestamp:
    @staticmethod
    def delta(other_timestamp: int) -> int:
        return current_timestamp() - other_timestamp

    @staticmethod
    def to_yyyy_mm_dd(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%Y{separator}%m{separator}%d')

    @staticmethod
    def to_yy_mm_dd(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%y{separator}%m{separator}%d')

    @staticmethod
    def to_dd_mm_yyyy(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{separator}%m{separator}%Y')

    @staticmethod
    def to_dd_mm_yy(timestamp: int, separator: str = '-') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{separator}%m{separator}%y')

    @staticmethod
    def to_hh_ii_ss(timestamp: int, separator: str = ':') -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%H{separator}%I{separator}%S')

    @staticmethod
    def to_yyyy_mm_dd_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%Y{date_separator}%m{date_separator}%d'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_yy_mm_dd_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%y{date_separator}%m{date_separator}%d'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_dd_mm_yyyy_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%Y'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')

    @staticmethod
    def to_dd_mm_yy_hh_ii_ss(
            timestamp: int,
            date_separator: str = '-',
            datetime_separator: str = ' ',
            time_separator: str = ':'
    ) -> str:
        return datetime.fromtimestamp(timestamp).strftime(f'%d{date_separator}%m{date_separator}%y'
                                       f'{datetime_separator}'
                                       f'%H{time_separator}%M{time_separator}%S')


def is_datetime(value: str) -> bool:
    return parse_any_date(value, on_error=OnError.IGNORE) is not None


@catch()
def parse_any_date(value: str) -> datetime | None:
    return date_parser.parse(value)


def maybe_from_iso(maybe_iso: str | None) -> datetime | None:
    if not maybe_iso:
        return None

    with suppress(Exception):
        return datetime.fromisoformat(maybe_iso)

    return None


def current_timestamp() -> int:
    return int(datetime.now().timestamp())


def current_hh_ii_ss(separator: str = ':') -> str:
    return datetime.now().strftime(f'%H{separator}%M{separator}%S')


def current_yyyy_mm_dd(separator: str = '-') -> str:
    return datetime.now().strftime(f'%Y{separator}%m{separator}%d')


def current_dd_mm_yyyy(separator: str = '-') -> str:
    return datetime.now().strftime(f'%d{separator}%m{separator}%Y')


def current_yy_mm_dd(separator: str = '-') -> str:
    return datetime.now().strftime(f'%y{separator}%m{separator}%d')


def current_dd_mm_yy(separator: str = '-') -> str:
    return datetime.now().strftime(f'%d{separator}%m{separator}%y')


def current_yyyy_mm_dd_hh_ii_ss(
        date_separator: str = '-',
        datetime_separator: str = ' ',
        time_separator: str = ':'
) -> str:
    return datetime.now().strftime(f'%Y{date_separator}%m{date_separator}%d'
                                   f'{datetime_separator}'
                                   f'%H{time_separator}%M{time_separator}%S')


def current_yy_mm_dd_hh_ii_ss(
        date_separator: str = '-',
        datetime_separator: str = ' ',
        time_separator: str = ':'
) -> str:
    return datetime.now().strftime(f'%y{date_separator}%m{date_separator}%d'
                                   f'{datetime_separator}'
                                   f'%H{time_separator}%M{time_separator}%S')


def current_dd_mm_yyyy_hh_ii_ss(
        date_separator: str = '-',
        datetime_separator: str = ' ',
        time_separator: str = ':'
) -> str:
    return datetime.now().strftime(f'%d{date_separator}%m{date_separator}%Y'
                                   f'{datetime_separator}'
                                   f'%H{time_separator}%M{time_separator}%S')


def current_dd_mm_yy_hh_ii_ss(
        date_separator: str = '-',
        datetime_separator: str = ' ',
        time_separator: str = ':'
) -> str:
    return datetime.now().strftime(f'%d{date_separator}%m{date_separator}%y'
                                   f'{datetime_separator}'
                                   f'%H{time_separator}%M{time_separator}%S')
