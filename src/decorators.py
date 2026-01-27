from functools import wraps


def log(filename=None):
    """Декоратор записи логов. Если передать аргумент, то результат работы записывается в файл. Иначе - в консоль"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                _ = func(*args, **kwargs)
                # Обработка с аргументом в файл
                if filename:
                    with open(f"{filename}", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                    return f"{func.__name__} ok\n"
                # Обработка без аргумента в консоль
                else:
                    print(f"{func.__name__} ok")
                return f"{func.__name__} ok"
            except Exception as e:
                # Обработка ошибки с аргументом в файл
                if filename:
                    with open(f"{filename}", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                # Обработка с ошибкой без аргумента в консоль
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

        return inner

    return wrapper
