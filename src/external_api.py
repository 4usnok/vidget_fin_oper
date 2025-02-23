import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def trans_value(bank_oper):
    code_currency = bank_oper["operationAmount"]["currency"]["code"]
    value_sum = bank_oper["operationAmount"]["amount"]
    if code_currency == "RUB":
        return float(value_sum)
    else:
        result = conv_value(value_sum, code_currency)
        return result

# Создадим функцию, которая будет отправлять API-запрос
def conv_value(amount, code_value):
    """
    Принимает на вход название валют EUR или USD и конвертирует в RUB
    """
    # Создадим переменную, в которую поместим ссылку на API
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{code_value}"
    response = requests.get(url)
    result = response.json()["conversion_rates"]["RUB"]
    return result * float(amount)


new_div = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

# Распечатаем на экран результат конвертирования валют в рубли
print(trans_value(new_div))
