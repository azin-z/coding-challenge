import functools
import time


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        print("{} took {} seconds".format(func.__name__, round(time.time() - start_time)))
        return output
    return wrapper
