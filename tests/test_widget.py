import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        # набор для теста
        ("2024-03-11T02:26:18.671407", "11.03.2024")
    ],
)
def test_get_date(info, expected):
    assert get_date(info) == expected


@pytest.mark.parametrize(
    "info, expected",
    [
        # первый набор для теста "номер"
        ("Visa Super 1234567890123456", "Visa Super 1234 56** **** 3456"),
        # второй набор для теста "Счет"
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected
