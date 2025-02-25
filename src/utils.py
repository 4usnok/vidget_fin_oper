import json
import logging


logger = logging.getLogger('utils.py')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('D:\\Projects_from_skypro\\PythonProject_1\\logs\\utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def func_json(file_path):
    """
    Функций принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях.
    """
    # Создадим условия, которые будут проверять файл
    # Если он пустой, содержит не список или не найден, функция возвращает пустой список.
    try:
        logger.info('Выполняем запрос с ключевыми словами: ')
        try:
            with open(file_path, encoding="utf-8") as json_file:
                result = json.load(json_file)
                if isinstance(result, list):
                    return result
                else:
                    return []

        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    except Exception as ex:
        logging.error(f'Произошла ошибка: {ex}')


print(func_json("D:\\Projects_from_skypro\\PythonProject_1\\data\\operations.json"))
