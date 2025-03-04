import collections
import re
import json


url_json = "E:\\Project_skypro\\DZ_1\\pythonProject\\proj_1\\data\\file_work.json"

list_json = []
list_new = []

with open(url_json, "r", encoding="utf-8") as json_file:
    json_reader = json.load(json_file)
    for row in json_reader:
        # Напишем цикл, который добавляет в пустой список словари исходя из условия
        list_json.append(row)


def filter_transactions_by_description(transactions, search_string):
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    # Для начала нужно раскрыть json файл
    for url_dict in transactions:
        # Напишем цикл, который перебирает словари
        if re.search(search_string, url_dict['state']):
                list_new.append(url_dict)
    return list_new


def count_operations_by_category(url_input_2, description):
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    # Создаём пустой список, в который будем добавлять новый словарь, требуемый по ТЗ
    list_for_dict = []
    # Создаём переменную для метода Counter для подсчёта значений для определенного ключа
    names_dict = collections.Counter()
    # Создаём цикл, который достанет словарь из списка
    for only_dict in url_input_2:
        # Создаём цикл, который будет перебирать ключи и значения словаря
        for key, val in only_dict.items():
            # Напишем условия, который будут определять наличие ключа из словаря в передаваемом списке
            if key in description:
                # Если условие True, тогда мы добавляем словарь в пустой список
                list_for_dict.append({key: val})
                # При совпадении значений, увеличим счетчик на 1
                names_dict[key] += 1

    return names_dict


print(filter_transactions_by_description(list_json, 'EXECUTED'))
print(count_operations_by_category(list_json, description=['date']))
