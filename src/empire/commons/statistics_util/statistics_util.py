import statistics
from typing import Iterable

from empire.commons.types_ import NumberType


class StatisticsUtil:
    @staticmethod
    def safe_fmean(data: Iterable[NumberType]) -> float:
        if not data:
            return 0.0

        if "fmean" not in dir(statistics):
            return statistics.mean(data)
        else:
            return statistics.fmean(data)
