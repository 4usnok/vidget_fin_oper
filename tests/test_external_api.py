from unittest.mock import patch
from src.external_api import trans_value




def test_trans_value_in_rub():
    new_div = {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }
    assert trans_value(new_div) == 31957.58


@patch('requests.get')
def test_trans_value_in_usd(mock_get):
    new_div = {
        "operationAmount": {
            "amount": "1",
            "currency": {
                "name": "доллар",
                "code": "USD"
            }
        }
    }
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 1}}
    assert trans_value(new_div) == 1.00
    #mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/0dcfcddbc57fc16eaa3d6607/latest/USD")

    # def test_conv_value(mock_get):
    #     mock_get.return_value.json.return_value = {'base_code': 'USD', 'conversion_rates': {'RUB': 1}}
    #     assert conv_value(1) == 1
    #     mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/0dcfcddbc57fc16eaa3d6607/latest/USD")