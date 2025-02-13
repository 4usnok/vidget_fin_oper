def log(filename):
    """
    Декоратор, который принимает параметр filename
    """

    def my_decorator(func):
        """
        Декоратор, который оборачивает функцию и добавляет дополнительное поведение.
        """

        def wrapper(*args):
            """
            Функция-обёртка, выполняющая дополнительные действия до и после вызова func.
            """
            result = func(*args)
            if not filename:
                my_file = open(filename, "w")
                my_file.write("my_function ok")
                my_file.close()
            else:
                print('my_function error: тип ошибки. Inputs: (1, 2), {}')
            return result

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
def my_function(x: int, y: int) -> int:
    """
    Декоратор суммирует параметры
    """
    return x + y


# Вызов функции
my_function(1, 2)
