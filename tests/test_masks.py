import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "info, expected",
    [
        # набор для теста
        ("73654108430135874305", "**4305")
    ],
)
def test_get_mask_account(info, expected):
    assert get_mask_account(info) == expected


@pytest.mark.parametrize(
    "info, expected",
    [
        # набор для теста
        ("7000792289606361", "7000 79** **** 6361")
    ],
)
def test_get_mask_card_number(info, expected):
    assert get_mask_card_number(info) == expected
