def debug(func):
    def wrapper(*args, **kwargs):
        arg_val = ', '.join(str(arg) for arg in args)
        key_val = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        if arg_val == '':
            arg_val="no arg value"
        print(f"Calling {func.__name__} with args -> {arg_val} and kwargs -> {key_val}")
        return func(*args, **kwargs)
    return wrapper

@debug
def _hello():
    print("Hello")

@debug
def hello(name, greet="Hi!"):
    print(f"{greet} {name}")


_hello()
hello("Pratik")
hello("Pratik", greet="Kemon achis,")