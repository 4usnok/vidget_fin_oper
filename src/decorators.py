def log(filename=None):
    """
    Декоратор, который принимает параметр filename
    """

    def my_decorator(func):
        """
        Декоратор, который оборачивает функцию и добавляет дополнительное поведение.
        """

        def wrapper(*args, **kwargs):
            """
            Функция-обёртка, выполняющая дополнительные действия до и после вызова func.
            """
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "r+") as file:
                        file.write(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. inputs: {args}, {kwargs}")
                else:
                    with open(filename, "r+") as file:
                        file.write(f"{func.__name__} error: {e}. inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


def predicate_log_positive(x, y):
    """
    Предикат проверяет на положительность
    """
    return x >= 0, y >= 0


def predicate_log_negative(x, y):
    """
    Предикат проверяет на отрицательность
    """
    return x <= 0, y <= 0


# Применение декоратора log
@log(filename="mylog.txt")
def my_function_file(x, y):
    return x + y


@log()
def my_function(x, y):
    return x + y
