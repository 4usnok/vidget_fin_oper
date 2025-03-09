import re

from src.generators import descriptions


def filter_by_state(set_of_dict: list, state: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию "EXECUTED"). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению state.
    """
    new_list = []
    for specific_dict in set_of_dict:
        for meaning in specific_dict:
            if specific_dict[meaning] == state:
                new_list.append(specific_dict)
    return new_list
    # Используя циклы, перебрал элементы списка, вследствие чего,
    # ввёл условие при котором, смог получить желаемые словари для нашей задачи


def sort_by_date(list_dict: list, reverse: bool=True) -> list:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    return sorted(list_dict, key=lambda word_key: word_key["date"], reverse=reverse)
    # Смог обойтись одним выражением, которое одновременно сортирует список словарей и разворачивает
    # Можно обойтись без reverse, но я как понял, в задании требуется именно развернуть


def filter_trans_by_des(list_dict: list, search_string: str) -> list:
    """
    Функция принимает транзакции и строку поиска, выводит список транзакций у которых есть данная строка
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [el_in_dict for el_in_dict in list_dict if pattern.search(el_in_dict.get("description", ""))]
