import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end= time.time()
        print(f"time taken - {end - start} by {func.__name__}")
        return result
    return wrapper

@timer
def example_timer(n):
    time.sleep(n)

example_timer(2)