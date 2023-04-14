from time import time

from empire.commons.throttling import Per, throttler, throttler_decorator


def test_throttling_method():
    def throttled(a):
        return f"{a} {int(time())}"

    a_throttled = throttler(throttled, 2, Per.SECOND)
    start_ = time()
    for i in range(10):
        result = a_throttled(i)
        assert (start_ - 1) <= int(result.split(" ")[1]) <= (start_ + 1)
        assert result.split(" ")[0] == str(i)
        start_ += 0.5


def test_throttling_decorator():
    @throttler_decorator(15, Per.MINUTE)
    def throttled(a):
        return f"{a} {int(time())}"

    start_ = time()
    for i in range(5):
        result = throttled(i)
        assert (start_ - 1) <= int(result.split(" ")[1]) <= (start_ + 1)
        assert result.split(" ")[0] == str(i)
        start_ += 4
