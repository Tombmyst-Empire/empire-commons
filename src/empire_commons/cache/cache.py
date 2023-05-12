"""
Cache service for Empire.
"""
import atexit
import logging
import os
from contextlib import suppress
from typing import Any, Callable, Final

from empire_commons.result_container import ResultContainer


class _LocalCache:
    def __init__(self):
        self._client = None

    @staticmethod
    def initializer():
        """
        Initializes the diskcache client
        """
        import pathlib  # pylint: disable=import-outside-toplevel

        from diskcache import FanoutCache  # pylint: disable=import-outside-toplevel

        cache_directory: str = os.path.join(str(pathlib.Path.home()), ".empire")
        os.makedirs(cache_directory, exist_ok=True)

        client = FanoutCache(os.path.join(cache_directory, "cache.dat"))
        atexit.register(_LocalCache.end, client)
        return client

    def get(self, cache_key: str, default: Any = None) -> Any:
        """
        Returns an item from cache
        :param cache_key: The cache key
        :param default: The default value if item does not exist
        :return: The item
        """
        return self._client.get(key=cache_key, default=default, retry=True)

    def set(self, cache_key: str, value: Any, time_to_live_in_seconds: int = 0) -> bool:
        """
        Sets an item in cache
        :param cache_key: The cache key
        :param value: The item to insert
        :param time_to_live_in_seconds: Time to live in seconds. You don't have to calculate the timestamp.
        :return: True on success, false otherwise
        """
        return self._client.set(
            key=cache_key,
            value=value,
            expire=None
            if time_to_live_in_seconds == 0
            else time_to_live_in_seconds,  # no need to add time to live to now, diskcache does it
            retry=True,
        )

    def cache_service_name(self) -> str:  # pylint: disable=no-self-use
        """
        Returns the service name
        """
        return "DiskCache.FanoutCache"

    @staticmethod
    def end(client):
        """
        Closes the client at the end of the program's execution
        """
        with suppress(Exception):
            client.close()


class MetaCache(type):
    """
    Cache metaclass.
    """

    def __new__(cls, name, bases, class_dict):
        clazz = super().__new__(cls, name, bases, class_dict)

        setattr(clazz, "_client", _LocalCache.initializer())
        setattr(clazz, "get", _LocalCache.get)
        setattr(clazz, "set", _LocalCache.set)
        setattr(clazz, "cache_service_name", _LocalCache.cache_service_name)

        return clazz


class _Cache(metaclass=MetaCache):
    """
    Dynamically built cache class.
    """

    def get(self, cache_key: str, default: Any = None) -> Any:
        """
        Returns "cache_key" from cache if it exists, otherwise it returns "default".
        """

    def set(self, cache_key: str, value: Any, time_to_live_in_seconds: int = 0) -> bool:
        """
        Sets "value" in cache at key "cache_key" and stores it for "time_to_live_in_second".
        If "time_to_live_in_seconds" is set to 0 (default value), it is stored indefinitely.

        Returns True on success, false otherwise
        """

    def cache_service_name(self) -> str:
        """
        Returns the cache service name.
        """


class _Instance:  # pylint: disable=too-few-public-methods
    _instance = None

    @staticmethod
    def get():  # pylint: disable=missing-function-docstring
        if not _Instance._instance:
            _Instance._instance = _Cache()
        return _Instance._instance


Cache = _Instance.get()  # pylint: disable=invalid-name


def cache_decorator(key_maker: Callable[[str, str], str] = lambda cache_prefix, query: f'{cache_prefix}:{query}'):
    """
    A decorator that removes the cache handling boilerplate code.

    This decorator must decorate the function that performs the slow code, like a call to an external API.

    Using the decorator makes the decorated function return the result in an instance of *ResultContainer*

    **The wrapper**

    The wrapper has few predefined parameters (and also allows custom parameters):

    - **logger**: A logger instance. It is passed to the decorated function to its *logger* parameter.
    - **query**:  The query to the external service. The wrapper does not care of the query except for making the cache key. It is passed to the
        decorated function to its *query* parameter.
    - **cache_prefix**: Prefixes every cache key. Allows using different cache entries for the same service and query.
    - **ignore_cache**: When True, the cache is completely ignored.
    - **force_cache_refresh**: When True, the decorated function is executed and the item in cache will be replaced.
    - **cache_time_to_live**: Specifies the number of seconds the item should be kept in cache.

    An example: ::

            @cache_decorator(lambda cache_prefix, query: f'{cache_prefix}:{query}')
            def forward_geocoding(
                    logger: logging.Logger,
                    query: str,
                    api_key: str,
                    result_language: str = GoogleSupportedLanguages.ENGLISH
            ) -> JsonType:
                geocoder_result: geocoder.api.GoogleQuery = geocoder.google(
                    query,
                    key=api_key or get_api_key_for_external_service(ExternalServicesApiKeys.GEOCODER),
                    language=result_language
                )

                if geocoder_result.ok:
                    return geocoder_result.geojson
                else:
                    logger.error(f'Geocoder response not ok! {geocoder_result.error}')
                    raise ExternalServiceError('geocoding', 'Erronous response from host')

    :param key_maker: A callable that is responsible for making the cache key. First parameter is the cache prefix and the second is the query.
        It must return a string.
    """

    def _cache(func):
        def wrapper(  # pylint: disable=too-many-arguments
            logger: logging.Logger,
            query: str,
            cache_prefix: str,
            ignore_cache: bool,
            force_cache_refresh: bool,
            cache_time_to_live: int,
            **kwargs,
        ) -> ResultContainer:
            cache_key: str = key_maker(cache_prefix, query)

            if ignore_cache is force_cache_refresh is False:
                if cached_data := Cache.get(cache_key):
                    logger.trace(f"Cache hit with query {query}")
                    return ResultContainer(cached_data, cache_hit=True)

            logger.trace(f"Calling {func.__qualname__}")
            result: Any = func(logger=logger, query=query, **kwargs)

            if not ignore_cache:
                if Cache.set(cache_key, result, cache_time_to_live):
                    logger.trace("Setting in cache")
                else:
                    logger.warning("Could not put item in cache")

            return ResultContainer(result)

        return wrapper

    return _cache


if __name__ == "__main__":
    assert Cache.cache_service_name() == "DiskCache.FanoutCache"
    assert Cache.set("test-patate", "cest un legume")
    assert Cache.get("test-patate") == "cest un legume"
    assert Cache.get("this key does not exist", "le default") == "le default"
