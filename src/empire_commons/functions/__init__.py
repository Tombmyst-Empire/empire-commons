from empire_commons.functions._deffered_call import DefferedCall, coalesce_deffered
from empire_commons.functions._conditional import maybe_enum, default, coalesce, or_raise, or_raise_broad
from empire_commons.functions._chaining import accumulate_callables
from empire_commons.functions._dummies import dummy_that_returns_none, dummy_that_does_nothing, dummy_that_returns_first_arg


__all__ = [
    'DefferedCall',
    'coalesce_deffered',
    'maybe_enum',
    'default',
    'coalesce',
    'or_raise',
    'or_raise_broad',
    'accumulate_callables',
    'dummy_that_returns_none',
    'dummy_that_does_nothing',
    'dummy_that_returns_first_arg'
]
