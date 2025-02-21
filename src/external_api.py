import os
import requests
from unittest.mock import patch
from dotenv import load_dotenv


load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

# Создадим функцию, которая будет отправлять API-запрос
def conv_value(amount: float, value: str) -> int:
    """
    Принимает на вход название валют EUR или USD и конвертирует в RUB
    """
    # Создадим переменную, в которую поместим ссылку на API
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{value}"
    response = requests.get(url)
    if response.json()['base_code'] == 'USD' or response.json()['base_code'] == 'EUR':
        result = response.json()['conversion_rates']['RUB']
        return result * amount

# Распечатаем на экран результат конвертирования валют в рубли
print(conv_value(2, 'USD'))


@patch('requests.get')
def test_conv_value(mock_get):
    mock_get.return_value.json.return_value = {'amount': 'value'}
    assert conv_value(1, 'USD') == 1
    mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD")