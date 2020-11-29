import sys

def inspect(func, *args):
    print(f"running {func.__name__}")
    val = func(*args)
    print(val)
    return val

def combine(a,b):
    return a+b

inspect(combine, 1, 2)

    