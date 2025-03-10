import unittest
from unittest.mock import mock_open, patch
from src.re_func import filter_transactions_by_description  # Замените на имя вашего модуля
import json

def test_filter_transactions_by_description():
    # Создаем фейковые данные для файла
    fake_file_content = json.dumps([
        {"amount": 100, "description": "Payment for groceries"},
        {"amount": 200, "description": "Restaurant bill"},
        {"amount": 50, "description": "Coffee shop"},
    ])

    # Используем mock_open для подмены открытия файла
    with patch("builtins.open", mock_open(read_data=fake_file_content)):
        # Читаем данные из фейкового файла
        with open("fake_transactions.json", "r") as file:
            transactions = json.load(file)

        # Вызываем тестируемую функцию
        result = filter_transactions_by_description(transactions, "Coffee")

        # Проверяем результат
        assert len(result) == 1
        assert result[0]["description"] == "Coffee shop"

if __name__ == "__main__":
    test_filter_transactions_by_description()
    print("All tests passed!")

