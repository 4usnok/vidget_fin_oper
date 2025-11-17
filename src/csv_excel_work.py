import csv

import pandas as pd
# Создадим по переменной, в которых пропишем относительные пути до наших файлов
path_csv = "data/transactions.csv"
path_excel = "data/transactions_excel.xlsx"


def csv_trans(path_only_csv):
    """
    Функция считывания финансовых операций файла с расширением CSV
    """
    new_list_csv = []
    with open(path_only_csv, encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        # Напишем цикл, который будет добавлять словари в наш пустой список
        for row in csv_reader:
            new_list_csv.append(row)
        return new_list_csv


def excel_trans(path_only_excel):
    """
    Функция считывания финансовых операций файла с расширением XLSX
    """
    df = pd.read_excel(path_only_excel)
    return df.to_dict(orient="records")


# print(excel_trans(path_excel))
# print(csv_trans(path_csv))

