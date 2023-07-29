from typing import Any, Callable

import ereport

from empire_commons.functions import DefferedCall
from empire_commons.on_error import OnError, handle_error2


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
        get_last_valid_result: bool = True
) -> Any:
    """
    Calls sequentially each *deffered*.

    :param break_at_first_none: When set True, as soon that a *deffered* returns None, returns
    :param break_at_first_false: When set True, as soon that a *deffered* returns False, returns
    :param break_at_first_falsy_value: When set True, as soon that a *deffered* returns a falsy value, returns
    :param on_error_behavior: On error behavior
    :param reporter: Reporter instance to pass to on error handler
    :param get_last_valid_result: When True, when a break configuration is encountered, returns last deffered result, otherwise, returns the current result
    """
    last_result: Any = None

    for a_deffered in deffered:
        current_result: Any = handle_error2(
            a_deffered.callable_,
            *a_deffered.star_args,
            on_error_behavior_=on_error_behavior,
            reporter_=reporter,
            **a_deffered.kwargs
        )

        if break_at_first_none and current_result is None:
            return last_result if get_last_valid_result else current_result
        elif break_at_first_false and current_result is False:
            return last_result if get_last_valid_result else current_result
        elif break_at_first_falsy_value and not current_result:
            return last_result if get_last_valid_result else current_result

        last_result = current_result

    return last_result
