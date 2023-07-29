from enum import Enum, auto
from typing import Any, Callable

import ereport

from empire_commons.functions import DefferedCall
from empire_commons.on_error import OnError, handle_error2


class ThenBreakValue(Enum):
    CURRENT = auto()
    LAST = auto()


def accumulate_callables(initial_value: Any, *callables: Callable) -> Any:
    """
    Takes *initial_value* and passes it to the first callable.

    The result of the first callable is passed to the second, and so on.
    """
    current: Any = initial_value
    for callable_ in callables:
        current = callable_(current)

    return current


def then(
        *deffered: DefferedCall,
        break_at_first_none: bool = False,
        break_at_first_false: bool = False,
        break_at_first_falsy_value: bool = False,
        on_error_behavior: OnError = OnError.RAISE,
        reporter: ereport.Reporter | None = None,
        value_to_return_on_break: ThenBreakValue | Any = ThenBreakValue.LAST
) -> Any:
    """
    Calls sequentially each *deffered*.

    :param break_at_first_none: When set True, as soon that a *deffered* returns None, returns
    :param break_at_first_false: When set True, as soon that a *deffered* returns False, returns
    :param break_at_first_falsy_value: When set True, as soon that a *deffered* returns a falsy value, returns
    :param on_error_behavior: On error behavior
    :param reporter: Reporter instance to pass to on error handler
    :param value_to_return_on_break: When a break condition occurs, returns either last value when *LAST*, current value when *CURRENT* or the provided value
    """
    last_result: Any = None

    def _get_break_value(current_value_: Any):
        if value_to_return_on_break == ThenBreakValue.LAST:
            return last_result
        elif value_to_return_on_break == ThenBreakValue.CURRENT:
            return current_value_
        else:
            return value_to_return_on_break

    for a_deffered in deffered:
        current_result: Any = handle_error2(
            a_deffered.callable_,
            *a_deffered.star_args,
            on_error_behavior_=on_error_behavior,
            reporter_=reporter,
            **a_deffered.kwargs
        )

        if break_at_first_none and current_result is None:
            return _get_break_value(current_result)
        elif break_at_first_false and current_result is False:
            return _get_break_value(current_result)
        elif break_at_first_falsy_value and not current_result:
            return _get_break_value(current_result)

        last_result = current_result

    return last_result
