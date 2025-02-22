from unittest.mock import patch
from src.external_api import conv_value


@patch('requests.get')
def test_conv_value(mock_get):
    mock_get.return_value.json.return_value = {'base_code': 'USD', 'conversion_rates': {'RUB': 1}}
    assert conv_value(1, 'USD') == 1
    mock_get.assert_called_once_with(f"https://v6.exchangerate-api.com/v6/0dcfcddbc57fc16eaa3d6607/latest/USD")

