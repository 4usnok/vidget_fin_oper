import pytest

from src.generators import card_number_generator, transaction_descriptions, filter_by_currency

@pytest.mark.parametrize(
    "info, expected", [
    ([{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount":
                {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }],
     [{
         "id": 939719570,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "operationAmount":
             {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации",
         "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702",
     }]
    )]
)
def test_filter_by_currency(info, expected):
    assert list(filter_by_currency(info, "USD")) == expected

@pytest.mark.parametrize(
    "info, expected", [
    ([
{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод от организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод на номер",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
     ],
        ["Перевод от организации",
         "Перевод на номер"])]
)
def test_transaction_descriptions(info, expected):
    assert list(transaction_descriptions(info)) == expected

@pytest.mark.parametrize(
    "info, expected", [
        # Набор для теста
        ((1, 5), [
        "0000 0000 0000 0001" ,
        "0000 0000 0000 0002" ,
        "0000 0000 0000 0003" ,
        "0000 0000 0000 0004" ,
        "0000 0000 0000 0005"
        ])
    ])
def test_card_number_generator(info, expected):
    assert list(card_number_generator(1, 5)) == expected
