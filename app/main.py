from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)

        return cache_store[key]

    return wrapper
