from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
import pytest


@pytest.mark.parametrize("number_card", ["7000792289606361"])
def test_get_mask_card_number(number_card):
    assert get_mask_card_number("7000792289606361")


@pytest.mark.parametrize("number_card_2", ["73654108430222135874"])
def test_get_mask_account(number_card_2):
    assert get_mask_account("73654108430222135874")


@pytest.mark.parametrize("number_card_3", ["1596837868705199"])
def test_mask_account_card(number_card_3):
    assert mask_account_card("1596837868705199")


@pytest.mark.parametrize(
    "set_of_dict, state",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
    ],
)
def test_filter_by_state(set_of_dict, state):
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )


@pytest.mark.parametrize(
    "list_dict",
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
)
def test_sort_by_date(list_dict):
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )


@pytest.mark.parametrize("data_num", ["2024-03-11T02:26:18.671407"])
def test_get_data(data_num):
    assert get_date("2024-03-11T02:26:18.671407")
