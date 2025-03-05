from datetime import datetime
import csv
from proj_1.src.csv_excel_work import new_list_excel
from proj_1.src.generators import transactions
from src.re_func import list_json



def main():
    hello_input = input(f'Привет! Добро пожаловать в программу работы с банковскими транзакциями. '
                        f'\nВыберите необходимый пункт меню:'
                        '\n1. Получить информацию о транзакциях из JSON-файла'
                        '\n2. Получить информацию о транзакциях из CSV-файла'
                        '\n3. Получить информацию о транзакциях из XLSX-файла'
                        '\n')

    if hello_input == '1':
        print('\nДля обработки выбран JSON-файл\n')
    elif hello_input == '2':
        print('\nДля обработки выбран CSV-файл\n')
    elif hello_input == '3':
        print('\nДля обработки выбран XLSX-файл\n')

    str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                      '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                      '\n')

    str_input_upper = str_input.upper()
    if str_input_upper in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')
    else:
        print(f'Статус операции {str_input_upper} недоступен. '
              f'\nВведите статус, по которому необходимо выполнить фильтрацию. '
              f'\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

# Сортируем по дате
# Отсортируем json
    if hello_input == '1':
        date_input = input('Отсортировать операции по дате? Да/Нет\n')
        if date_input == 'Да':
            sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
            if sort_order == 'по возрастанию':
                print(sorted(list_json, key=lambda x: x["date"], reverse=False))
            elif sort_order == 'по убыванию':
                print(sorted(list_json, key=lambda x: x["date"], reverse=True))


# Отсортируем csv
    elif hello_input == '2':
        with open(r'E:\Project_skypro\DZ_1\pythonProject\proj_1\data\transactions.csv',
                  newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for transaction in transactions:
                if 'date' in transaction:
                    transaction['date'] = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S')
                date_input = input('Отсортировать операции по дате? Да/Нет\n')
                if date_input == 'Да':
                    sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
                    if sort_order == 'по возрастанию':
                        sorted_transactions = sorted(transactions, key=lambda x: x['date'], reverse=False)
                        print(sorted_transactions)
                    elif sort_order == 'по убыванию':
                        sorted_transactions = sorted(transactions, key=lambda x: x['date'], reverse=True)
                        print(sorted_transactions)

# Отсортируем excel
#     elif hello_input == '3':
#         date_input = input('\nОтсортировать операции по дате? Да/Нет\n')
#         if date_input == 'Да':
#             sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
#             if sort_order == '\nпо возрастанию\n':
#                 print(sorted(new_list_excel, key=lambda x: x["date"], reverse=False))
#             if sort_order == '\nпо убыванию\n':
#                 print(sorted(new_list_excel, key=lambda x: x["date"], reverse=True))




if __name__ == '__main__':
    print(main())
