import json
import os


def func_json(file_path: str) -> str:
    """
    Функций принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях.
    """
    # Создадим условия, которые будут проверять файл
    # Если он пустой, содержит не список или не найден, функция возвращает пустой список.
    try:
        with open(file_path, encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

print(func_json("D:\\Projects_from_skypro\\PythonProject_1\\data\\operations.json"))
