import pytest
from src import decorators


def test_log(capsys):
    captured = capsys.readouterr()
    assert captured.out == "my_function error: тип ошибки. Inputs: (1, 2), {}"