from functools import lru_cache

from lesson7.trace import trace_explorer


@lru_cache(maxsize=4096)
@trace_explorer(max_level_to_display=-1)
def fib(n):
    if n <= 1:
        return n
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@trace_explorer(max_level_to_display=1)
def test_recurcive(lvl):
    if lvl > 0:
        test_recurcive(lvl-1)
    return lvl


# print(fib(30))
# print("\n")
# test_recurcive(400)

print([fib(i) for i in range(100)])
