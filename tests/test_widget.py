import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("type_and_number, expected",
                         [("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
                          ("Счет 73654108430135874305", "**4305"),
                          ("Maestro 7000792289606361", "7000 79** **** 6361"),
                          ("Счет нерезидента 12345123455678956789", "**6789")])
def test_mask_account_card(type_and_number, expected):
    assert mask_account_card(type_and_number) == expected


@pytest.mark.parametrize("type_and_number",
                         ["",
                          "123132",
                          "12345678912345678",
                          "123451234512345123451"])
def test_mask_account_card_wrong_value_error(type_and_number):
    with pytest.raises(ValueError):
        mask_account_card(type_and_number)


@pytest.mark.parametrize("type_and_number",
                         [123124,
                          [12345],
                          (12345),
                          {"key": "value"}])
def test_mask_account_card_wrong_attribute_error(type_and_number):
    with pytest.raises(AttributeError):
        mask_account_card(type_and_number)


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("raw_date",
                         ["",
                          "some_text"])
def test_get_date_wrong_date_format(raw_date):
    with pytest.raises(ValueError):
        get_date(raw_date)


@pytest.mark.parametrize("raw_date",
                         [[1, 2, 3],
                          (1, 2, 3),
                          {"key": "value"}])
def test_get_date_wrong_type_format(raw_date):
    with pytest.raises(TypeError):
        get_date(raw_date)
