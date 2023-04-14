import logging
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Callable, Sequence, Any, Optional


def thread_pool_execute(
        job: Callable,
        *job_args: Sequence[Any],
        number_of_workers: int = None,
        value_on_error: Any = None,
        job_timeout_in_seconds: int = 60,
        log_futures_exceptions: Optional[Callable] = logging.error,
        raise_on_futures_exceptions: bool = False
) -> list[Any]:
    """
    Executes blocking operations simultaneously using *ThreadPoolExecutor*.

    :param job: A callable to be called for each *job_args*
    :param job_args: Sequence of args (must be positional) to pass to each job
    :param number_of_workers: Number of "threads"
    :param value_on_error: Value that a job shall return on failure
    :param job_timeout_in_seconds:
    :param log_futures_exceptions:
    :param raise_on_futures_exceptions:
    :return:
    """
    with ThreadPoolExecutor(max_workers=number_of_workers) as pool:
        futures: list[Future] = [pool.submit(job, *args) for args in job_args]

    results: list[Any] = []

    for future in futures:
        results.extend(_maybe_future(
            future,
            value_on_error,
            job_timeout_in_seconds,
            log_futures_exceptions,
            raise_on_futures_exceptions
        ))

    return results


def _maybe_future(
        future: Future,
        value_on_error: Any,
        job_timeout_in_seconds: int,
        log_futures_exceptions: Optional[Callable],
        raise_on_futures_exceptions: bool
) -> Any:
    try:
        return future.result(job_timeout_in_seconds)
    except Exception as error:
        if log_futures_exceptions is not None:
            log_futures_exceptions('A job failed: %s', error)

        if raise_on_futures_exceptions:
            raise error
        return value_on_error
