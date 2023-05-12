import asyncio
from typing import Coroutine, Sequence, TypeVar

from empire_commons import list_util

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


async def all_(*coros: Coroutine[T, U, V]) -> Sequence[V]:
    return await asyncio.gather(*coros)


async def all_by_batch(*coros: Coroutine[T, U, V], batch_size: int) -> Sequence[V]:
    results: list[V] = []
    for batch in list_util.chunk_list(list(coros), batch_size):
        results.extend(await all_(*batch))

    return results
