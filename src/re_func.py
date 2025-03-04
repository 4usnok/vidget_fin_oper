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


def filter_transactions_by_description(url_input, str_input):
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    # Для начала нужно открыть и прочитать json файл
    for url_dict in url_input:
        # Напишем цикл, который перебирает словари
        for key, value in url_dict.items():
            if value == str_input:
                # В условии, напишем регулярное выражение, которое будет добавлять в пустой список словари
                if re.search(r"[a-zA-Z0-9_.+-]+", value):
                    list_new.append(url_dict)
    return list_new


def count_operations_by_category(url_input_2, description):
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    # Создаём пустой список, в который будем добавлять новый словарь, требуемый по ТЗ
    list_for_dict= []
    # Создаём переменную для метода Counter для подсчёта значений для определенного ключа
    names_dict = collections.Counter()
    # Создаём цикл, который достанет словарь из списка
    for dict_in_list in url_input_2:
        # Создаём цикл, который будет перебирать ключи и значения словаря
        for key, val in dict_in_list.items():
            # Напишем условия, который будут определять наличие ключа из словаря в передаваемом списке
            if key in description:
                # Если условие True, тогда мы добавляем словарь в пустой список
                list_for_dict.append({key: val})
                # При совпадении значений, увеличим счетчик на 1
                names_dict[key] += 1

    return names_dict


print(filter_transactions_by_description(list_json, 'EXECUTED'))
print(count_operations_by_category(list_json, description=['date']))
