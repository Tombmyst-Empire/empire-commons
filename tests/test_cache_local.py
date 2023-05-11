from time import sleep

from empire_commons.commons.cache import Cache


def test_cache_service_name():
    assert Cache.cache_service_name() == "DiskCache.FanoutCache"


def test_cache_set_get():
    assert Cache.set("test-patate", "cest un legume")
    assert Cache.get("test-patate") == "cest un legume"
    assert Cache.get("this key does not exist", "le default") == "le default"


def test_cache_set_time_to_live():
    assert Cache.set("test-patate", "cest un legume", 1)
    sleep(1.1)
    assert Cache.get("test-patate") is None
