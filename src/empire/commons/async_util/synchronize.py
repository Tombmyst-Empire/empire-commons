import asyncio
import atexit
import threading

_loop = None
_thread = None


def _get_default_event_loop():
    global _loop, _thread
    if _thread is None:
        if _loop is None:
            _loop = asyncio.get_event_loop()
        if not _loop.is_running():
            _thread = threading.Thread(
                target=_loop.run_forever,
                daemon=True)
            _thread.start()
    return _loop


def _set_default_event_loop(loop):
    stop_default_event_loop()
    _loop = loop


def start_default_event_loop():
    _get_default_event_loop()


@atexit.register
def stop_default_event_loop():
    global _loop, _thread
    if _loop is not None:
        _loop.call_soon_threadsafe(_loop.stop)  # noqa
    if _thread is not None:
        _thread.join()  # noqa
        _thread = None


def synchronize_coroutine(coroutine, loop=None):
    """
    class async_class:
        async def method(self):
            return True
    async_object = async_class()

    # wait for a coroutine
    sync_result = sync.coroutine(async_object.method())

    assert sync_result is True
    """
    if loop is None:
        loop = _get_default_event_loop()
    future = asyncio.run_coroutine_threadsafe(coroutine, loop)
    result = future.result()
    return result


def synchronize_function(function, loop=None):
    """
    class async_class:
        async def method(self):
            return True
    async_object = async_class()

    # wrap a single async callable
    sync_function = sync.function(async_object.method)

    assert sync_function() is True
    """
    def call(*params, **kwparams):
        async_coroutine = function(*params, **kwparams)
        return synchronize_coroutine(async_coroutine, loop)
    return call


class synchronize_methods:  # noqa
    """
    Synchronizes calls to async methods of an object.

    # an async object method to demonstrate use
    class async_class:
        async def method(self):
            return True
    async_object = async_class()

    # wrap all async methods of an object
    sync_object = sync.methods(async_object)

    assert sync_object.method() is True
    """
    def __init__(self, object, loop=None):
        self.__object = object
        self.__loop = loop

    def __getattr__(self, name):
        result = getattr(self.__object, name)
        if asyncio.iscoroutinefunction(result):
            return synchronize_function(result, self.__loop)
        else:
            return result
