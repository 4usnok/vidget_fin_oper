import pytest
import tempfile
from src.utils import func_json

@pytest.mark.parametrize("content, expected", [
    ("""[{"id": 441945886, "state": "EXECUTED"}]""", [{"id": 441945886, "state": "EXECUTED"}]),
    ("""[]""", []),
])
def test_func_json(content, expected):
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8') as temp_file:
        temp_file.write(content)
        temp_file.seek(0)  # Вернуться в начало файла для чтения
        assert func_json(temp_file.name) == expected
