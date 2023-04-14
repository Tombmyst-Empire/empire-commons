import asyncio
from empire.commons.async_util.synchronize import synchronize_methods, synchronize_function, synchronize_coroutine


class AsyncClass:
    async def async_method(self):
        await asyncio.sleep(0.1)
        return 1


async_class = AsyncClass()


async def async_function():
    await asyncio.sleep(0.1)
    return 2


def test_synchronize_methods():
    sync_object = synchronize_methods(async_class)
    assert sync_object.async_method() == 1


def test_synchronize_function():
    sync_function = synchronize_function(async_function)
    assert sync_function() == 2


def test_synchronize_coroutine():
    assert synchronize_coroutine(async_function()) == 2
