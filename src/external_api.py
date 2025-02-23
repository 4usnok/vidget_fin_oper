import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


# Создадим функцию, которая будет отправлять API-запрос
def conv_value(amount):
    """
    Принимает на вход название валют EUR или USD и конвертирует в RUB
    """
    # Создадим переменную, в которую поместим ссылку на API
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    if response.json()["base_code"] == "USD" or response.json()["base_code"] == "EUR":
        result = response.json()["conversion_rates"]["RUB"]
        return result * amount


# Распечатаем на экран результат конвертирования валют в рубли
print(conv_value(3))
