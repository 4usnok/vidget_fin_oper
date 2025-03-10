from src.utils import func_json
from src.csv_excel_work import csv_trans, excel_trans
from src.processing import filter_by_state
from src.generators import filter_by_currency, filter_by_currency_csv_and_excel
from src.processing import sort_by_date, filter_trans_by_des
from src.widget import mask_account_card

# Напишем приветственную логику
res_list = []


def main() -> None:
    hello_input = input('Привет! Добро пожаловать в программу работы с банковскими транзакциями. '
                        '\nВыберите необходимый пункт меню:'
                        '\n1. Получить информацию о транзакциях из JSON-файла'
                        '\n2. Получить информацию о транзакциях из CSV-файла'
                        '\n3. Получить информацию о транзакциях из XLSX-файла'
                        '\n')
# Напишем логику для выбора файла
    if hello_input == '1':
        print('\nДля обработки выбран JSON-файл\n')
        transactions = func_json("data/operations.json")
    elif hello_input == '2':
        print('\nДля обработки выбран CSV-файл\n')
        transactions = csv_trans("data/transactions.csv")
    elif hello_input == '3':
        print('\nДля обработки выбран XLSX-файл\n')
        transactions = excel_trans("data/transactions_excel.xlsx")

    while True:
        str_input = input('Введите статус, по которому необходимо выполнить фильтрацию. '
                          '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'
                          '\n')
        str_input_upper = str_input.upper()
        if str_input_upper in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, str_input_upper)
            print(f'\nОперации отфильтрованы по статусу {str_input_upper}\n')
            break
        else:
            print(f"Статус операции {str_input} недоступен.")

# Сортировка по дате и по её возрастанию/убыванию

    while True:
        date_input = input('Отсортировать операции по дате? Да/Нет\n')
        if date_input.upper() == 'Да'.upper():
            sort_order = input('\nОтсортировать по возрастанию или по убыванию?\n')
            if sort_order.upper() == 'по возрастанию'.upper():
                transactions = sort_by_date(transactions, reverse=False)
                break
            elif sort_order.upper() == 'по убыванию'.upper():
                transactions = sort_by_date(transactions)
                break
        else:
            print(f"Значение {str_input} недоступен.")

# Сортировка по рублям
    while True:
        sort_rub = input('\nВыводить только рублевые транзакции? Да/Нет\n')
        if sort_rub.upper() == 'Да'.upper():
            if hello_input == "1":
                transactions = list(filter_by_currency(transactions, "RUB"))
            else:
                transactions = list(filter_by_currency_csv_and_excel(transactions, "RUB"))
            break
        elif sort_rub.upper() == 'Нет'.upper():
            break
        else:
            print('Ответ некорректный')

    while True:
        input_word = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if input_word.upper() == 'Да'.upper():
            input_word = input("Введите слово: ")
            transactions = list(filter_trans_by_des(transactions, input_word))
            break
        elif input_word.upper() == 'Нет'.upper():
            break

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for trans in transactions:
            print(f"\n{trans.get("date", "")} {trans.get("description", "")}")
            if "from" in trans and type(trans["from"]) is str:
                print(f"{mask_account_card(trans.get("to", ""))} -> {mask_account_card(trans.get("from", ""))}")
            else:
                print(f"{mask_account_card(trans.get("to", ""))}")
            if "operationAmount" in transactions:
                print(
                    f"Сумма: {trans.get('operationAmount', '').get('amount', '')} "
                    f"{trans.get('operationAmount', '').get('currency', '').get('name', '')}"
                )
            else:
                print(
                    f"Сумма: {trans.get('amount', '')} "
                    f"{trans.get('currency_name', '')}")
    return


if __name__ == '__main__':
    main()
