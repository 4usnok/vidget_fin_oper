import os
import json


def func_json(file_path):
    if not os.stat(file_path).st_size == 0:
        with open(file_path, encoding='utf-8') as json_file:
            return json.load(json_file)
    elif os.stat(file_path).st_size == 0:
        return '[]'

print(func_json('D:\\Projects_from_skypro\\PythonProject_1\\data\\operations.json'))
