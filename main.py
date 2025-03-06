import csv
import json
import pandas as pd
from src.utils import func_json
from src.csv_excel_work import csv_trans, excel_trans
from src.processing import filter_by_state

def main():
    hello_input = input(f'Привет! Добро пожаловать в программу работы с банковскими транзакциями. '
                        f'\nВыберите необходимый пункт меню:'
                        '\n1. Получить информацию о транзакциях из JSON-файла'
                        '\n2. Получить информацию о транзакциях из CSV-файла'
                        '\n3. Получить информацию о транзакциях из XLSX-файла'
                        '\n')

    if hello_input == '1':
        print('\nДля обработки выбран JSON-файл\n')
        transactions = func_json("data/operations.json")
    elif hello_input == '2':
        print('\nДля обработки выбран CSV-файл\n')
        transactions = csv_trans("data/transactions.csv")
    elif hello_input == '3':
        print('\nДля обработки выбран XLSX-файл\n')
        transactions = excel_trans("data/transactions_excel.xlsx")

    str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                      '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                      '\n')

    str_input_upper = str_input.upper()
    if str_input_upper in {"EXECUTED", "CANCELED", "PENDING"}:
        transactions_filter_status = filter_by_state(transactions, str_input_upper)
        print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')
    else:
        while str_input_upper not in {"EXECUTED", "CANCELED", "PENDING"}:
            print(f"Статус операции {str_input} недоступен.")
            str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                              '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                              '\n')
            str_input_upper = str_input.upper()
            transactions_filter_status = filter_by_state(transactions, str_input_upper)
            print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')


# Сортируем по дате:
# Отсортируем json
    if hello_input == '1':
        date_input = input('Отсортировать операции по дате? Да/Нет\n')
        if date_input.upper() == 'Да'.upper():
            sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
            if sort_order.upper() == 'по возрастанию'.upper():
                with open('data/file_work.json', encoding="utf-8") as json_file:
                    result = json.load(json_file)
                    print(sorted(result, key=lambda x: x["date"], reverse=False))
            elif sort_order.upper() == 'по убыванию'.upper():
                with open('data/file_work.json', encoding="utf-8") as json_file:
                    result = json.load(json_file)
                    print(sorted(result, key=lambda x: x["date"], reverse=True))

# Отсортируем csv
    elif hello_input == '2':
        with open(r'data/transactions.csv', 'r', encoding='utf-8') as csv_file:
            sorter = list(csv.DictReader(csv_file, delimiter=';'))
            date_input = input('Отсортировать операции по дате? Да/Нет\n')
            if date_input.upper() == 'Да'.upper():
                sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
                if sort_order.upper() == 'по возрастанию'.upper():
                    result = sorted(sorter, key=lambda x: x["date"], reverse=False)
                    for rise in result:
                        print(rise)
                elif sort_order.upper() == 'по убыванию'.upper():
                    result = sorted(sorter, key=lambda x: x["date"], reverse=True)
                    for decline in result:
                        print(decline)

# Отсортируем excel
    elif hello_input == '3':
        workbook = pd.read_excel('data/transactions_excel.xlsx')
        string_book = str(workbook['date'])
        result = sorted(workbook, key=lambda x: x[string_book], reverse=True)
        print(result)






if __name__ == '__main__':
    print(main())
