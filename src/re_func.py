import collections
import json
import re


def filter_transactions_by_description(transactions: dict, search_string: str) -> list:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    list_new = []
    # Напишем цикл, который пройдётся по списку словарей
    for url_dict in transactions:
    # По условию, если строка присутствует в словаре или есть первое вхождение, тогда добавляется в список словарь
        if "description" in url_dict and re.search(search_string, url_dict["description"]):
            list_new.append(url_dict)
    return list_new


def count_operations_by_category(transactions:list, descriptions: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_desc = []
    for transaction in transactions:
    # Напишем условие, при котором происходит подсчёт значений заданных ключей
        if "description" in transaction and transaction["description"] in descriptions:
            list_desc.append(transaction["description"])
    return collections.Counter(list_desc)


if __name__ == "__main__":
    with open("../data/operations.json", "r", encoding="utf-8") as json_file:
        list_json = json.load(json_file)
    print(filter_transactions_by_description(list_json, "Перевод организации"))
    print(count_operations_by_category(list_json, ["Открытие вклада", "Перевод организации"]))
