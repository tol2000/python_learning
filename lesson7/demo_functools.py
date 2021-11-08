from functools import lru_cache, wraps

from lesson7.trace import trace_explorer


def tol_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        # ??? func(*args) always calls, even if key already present in cache
        # may be< set lazy computing?..
        cache.setdefault(args, func(*args))
        return cache[args]

    return wrapper


def tol1_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if not cache.keys().__contains__(args):
            cache.setdefault(args, func(*args))
        return cache[args]

    return wrapper


def my_lru_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            pass
        res = func(*args)
        cache[args] = res
        return res

    return wrapper


# instead of previous with two returns and no-needed pass )
def my_lru_cache_corr(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        try:
            res = cache[args]
        except KeyError:
            res = func(*args)
            cache[args] = res
        return res

    return wrapper


@my_lru_cache_corr
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

max_v = 1000

list1 = [fib(i) for i in range(max_v)]

print(f'{list1[0]}..{list1[max_v-1]}')
print(f'{list1[0]}..{list1[max_v-1]+1}')
print(f'{type(list1[0])}..{type(list1[max_v-1])}')
