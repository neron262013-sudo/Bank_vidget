from fileinput import filename
from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(f"{filename}", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                    return f"{func.__name__} ok\n"
                else:
                    print(f"{func.__name__} ok")
                return f"{func.__name__} ok"
            except Exception as e:
                if filename:
                    with open(f"{filename}", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
        return inner
    return wrapper


@log()
def my_function(x, y):
    return x + y

my_function("1", 2)