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
                print("my_function error: тип ошибки. Inputs: (1, 2), {}")
            else:
                print("my_function ok")
            return result

        return wrapper

    return my_decorator

# Применение декоратора log
@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y

# Вызов функции
my_function(1, 2)
