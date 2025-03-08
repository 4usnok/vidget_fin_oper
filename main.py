from datetime import datetime

from src.utils import func_json
from src.csv_excel_work import csv_trans, excel_trans
from src.processing import filter_by_state
from src.generators import filter_by_currency

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
    if str_input_upper in ["EXECUTED", "CANCELED", "PENDING"]:
        trans_filter_status = filter_by_state(transactions, str_input_upper)
        print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')
    else:
        while str_input_upper not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {str_input} недоступен.")
            str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                              '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                              '\n')
            str_input_upper = str_input.upper()
            trans_filter_status = filter_by_state(transactions, str_input_upper)
            print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')

# Отсортируем json
# Отсортируем по дате и по возрастанию/убыванию
    if hello_input == '1':
        date_input = input('Отсортировать операции по дате? Да/Нет\n')
        if date_input.upper() == 'Да'.upper():
            sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
            if sort_order.upper() == 'по возрастанию'.upper():
                transactions_filter_status = sorted(trans_filter_status, key=lambda x: x["date"], reverse=False)
            elif sort_order.upper() == 'по убыванию'.upper():
                transactions_filter_status = sorted(trans_filter_status, key=lambda x: x["date"], reverse=True)
# Отсортируем только по рублям
    sort_rub = input('\nВыводить только рублевые тразакции? Да/Нет\n')
    if sort_rub.upper() == 'Да'.upper():
        trans_rub = filter_by_currency(transactions_filter_status, "RUB")
        for transaction in trans_rub:
            print(transaction)
            # word_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            # if word_input.upper() == "Да".upper():
            #     print(transaction['state'])


if __name__ == '__main__':
    print(main())
