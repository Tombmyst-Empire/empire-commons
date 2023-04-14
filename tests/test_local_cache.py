from empire.commons.cache import Cache


def test_local_cache():
    assert Cache.cache_service_name() == 'DiskCache.FanoutCache'
    assert Cache.set('test-patate', 'cest un legume')
    assert Cache.get('test-patate') == 'cest un legume'
    assert Cache.get('this key does not exist', 'le default') == 'le default'
