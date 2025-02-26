from unittest.mock import patch, mock_open
from src.csv_excel_work import csv_trans, excel_trans
import csv
import pandas as pd


# Напишем тесты для функции csv_trans
def test_csv_trans():
    mock_data_scv = ("id,state,date,amount,currency_name,currency_code,from,to,description"
                 "\n650703,EXECUTED,2023-09-05T11:30:32Z,16210,Sol,PEN,Счет 58803664561298323391,"
                 "Счет 39745660563456619397,Перевод организации"
                 )

    with patch('builtins.open', mock_open(read_data=mock_data_scv)):
        result = list(csv.DictReader(open(csv_trans('fake_dir//fake_csv.csv'))))
        expected_result = [
            {'id': '650703',
             'state': 'EXECUTED',
             'date': '2023-09-05T11:30:32Z',
             'amount': '16210',
             'currency_name': 'Sol',
             'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391',
             'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'
             }
        ]
        assert result == expected_result

# Напишем тесты для функции excel_trans
mock_data = [
    {
        'id': [650703, 3598919, 593027],
        'state': ['EXECUTED', 'EXECUTED', 'CANCELED']
    }
]
df = pd.DataFrame(mock_data)

@patch('pandas.read_excel', return_value=df)
def test_excel_trans(mock_read_excel):
    result = pd.read_excel(excel_trans('fake_dir//fake_xlsx.xlsx'))
    expected_result = [
        {
            'id': [650703, 3598919, 593027],
            'state': ['EXECUTED', 'EXECUTED', 'CANCELED']
        }
    ]
    assert result.to_dict(orient='records') == expected_result
