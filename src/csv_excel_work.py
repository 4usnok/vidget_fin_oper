import csv

import pandas as pd
# Создадим по переменной, в которых пропишем относительные пути до наших файлов
path_csv = "D:\\Projects_from_skypro\\PythonProject_1\\data\\transactions.csv"
path_excel = "D:\\Projects_from_skypro\\PythonProject_1\\data\\transactions_excel.xlsx"
new_list_csv = []
new_list_excel = []


def csv_trans(path_only_csv):
    """
    Функция считывания финансовых операций файла с расширением CSV
    """
    with open(path_only_csv, "r", newline="") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        # Напишем цикл, который будет добавлять словари в наш пустой список
        for row in csv_reader:
            new_list_csv.append(row)
        return new_list_csv


def trans_excel(path_only_excel):
    """
    Функция считывания финансовых операций файла с расширением XLSX
    """
    df = pd.read_excel(path_only_excel)
    df_1 = df.to_dict()
    # Добавим в пустой список наши словари
    new_list_excel.append(df_1)
    return new_list_excel


print(trans_excel(path_excel))
print(csv_trans(path_csv))
