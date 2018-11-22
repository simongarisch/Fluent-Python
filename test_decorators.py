import functools

def double(func):
    print("running the function 'double'!")
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return inner

@double
def add(a, b):
    return a + b
