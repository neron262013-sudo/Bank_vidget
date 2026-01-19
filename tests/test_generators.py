import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def list_of_dicts():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency_usd(list_of_dicts):
    generator = filter_by_currency(list_of_dicts, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_no_currency(list_of_dicts):
    generator = filter_by_currency(list_of_dicts, "some text")
    assert next(generator) == "Нет указанной валюты"


def test_test_filter_by_currency_empty_list():
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Список транзакций пуст"


def test_transaction_descriptions(list_of_dicts):
    generator = transaction_descriptions(list_of_dicts)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list():
    generator = transaction_descriptions([])
    assert next(generator) == "Список транзакций пуст"


def test_card_number_generator():
    generator = card_number_generator(1, 2)
    assert next(generator) == "0000 0000 0000 0001" or "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0001" or "0000 0000 0000 0002"
    assert next(generator) == "Номера в указанном диапазоне закончились"
    assert next(generator) == "Номера в указанном диапазоне закончились"

def test_card_number_generator_invalid_start():
    generator = card_number_generator(-1, 10)
    assert next(generator) == "Недопустимый диапазон значений"

def test_card_number_generator_invalid_stop():
    generator = card_number_generator(1, -10)
    assert next(generator) == "Недопустимый диапазон значений"

def test_card_number_generator_start_less_stop():
    generator = card_number_generator(10, 1)
    assert next(generator) == "Недопустимый диапазон значений"




