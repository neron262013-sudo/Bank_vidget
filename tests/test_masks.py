import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


@pytest.mark.parametrize("card_number", [123, 12345678912345678, None])
def test_get_mask_card_number_not_16_digits(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


# @pytest.mark.parametrize("card_number", [123456789.1234567, [1234, 5678, 9123, 4567], "1234567891234567"])
# def test_get_mask_card_number_wrong_types(card_number):
#     with pytest.raises(ValueError):
#         get_mask_card_number(card_number)


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"


@pytest.mark.parametrize("account_number", [123, 123451234512345123451, None])
def test_get_mask_account_number_not_20_digits(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


# @pytest.mark.parametrize("account_number", [123451234512345.12345, [1234, 5678, 1234, 5678], "12345123451234512345"])
# def test_get_mask_account_number_wrong_types(account_number):
#     with pytest.raises(ValueError):
#         get_mask_account(account_number)
