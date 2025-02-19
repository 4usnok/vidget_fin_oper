import requests


name_usd = 'USD'
name_eur = 'EUR'
to = 'RUB'

def func_conv(amount: float) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    """
    # Первый делом создадим переменные, в которые заключим
    # Наши API-ключи
    url_usd = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={name_usd}&amount={amount}"
    url_eur = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={name_eur}&amount={amount}"
    # Создадим условия, которые буду принимать и проверять, какую валюту нам нужно конвертировать в RUB
    if name_usd == 'USD':
        payload = {}
        headers = {
            "apikey": "RlhFpAI7yYNl6Dj6flaYKxE3ye2A6d3g"
        }
        response_1 = requests.request("GET", url_usd, headers=headers, data=payload)
        status_code_1 = response_1.status_code
        result_1 = response_1.text
        data_1 = response_1.json()
        return data_1['result']
    elif name_eur == 'EUR':
        payload = {}
        headers = {
            "apikey": "RlhFpAI7yYNl6Dj6flaYKxE3ye2A6d3g"
        }
        response_2 = requests.request("GET", url_eur, headers=headers, data=payload)
        status_code_2 = response_2.status_code
        result_2 = response_2.text
        data_2 = response_2.json()
        return data_2['result']


print(func_conv(1))
