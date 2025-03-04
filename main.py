import re

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.re_func import new_func, new_func_2
import json


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
         print('\nДля обработки выбран XLSX-файла\n')

     str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                       '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                       '\n')
     str_input_upper = str_input.upper()
     if str_input_upper:
         print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')
     else:
         print(f'Статус операции {str_input_upper} недоступен. '
               f'\nВведите статус, по которому необходимо выполнить фильтрацию. '
               f'\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')


    date_input = input('Отсортировать операции по дате? Да/Нет')
    if date_input == 'Да':
        print("Операции будут отсортированы по дате.")
    else:
        print("Операции не будут отсортированы по дате.")


if __name__ == '__main__':
    print(main())
