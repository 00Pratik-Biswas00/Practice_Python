import time

def cache_decorator(func):
    cache_item = {}
    def wrapper(*args):
        if args in cache_item:
            return cache_item[args]
        result = func(*args)
        cache_item[args] = result
        return result
    return wrapper

@cache_decorator
def long_running_function(a, b):
    time.sleep(3)
    return a+b

print(long_running_function(8,7))
print(long_running_function(8,7))
print(long_running_function(8,7))