def filter_by_state(set_of_dict: list, state="EXECUTED") -> list:
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
