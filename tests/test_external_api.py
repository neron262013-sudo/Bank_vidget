from unittest.mock import Mock, patch

import pytest
from requests import ReadTimeout

from src.external_api import transaction_amount


@pytest.fixture
def test_response():
    return {"rates": {"USD": 1.1, "EUR": 1, "RUB": 100}}


@pytest.fixture
def test_transaction_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@pytest.mark.parametrize("transaction, expected",
                         [({"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}},
                           31957.58),
                          ({"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}},
                           10000.00),
                          ({"operationAmount": {"amount": "50", "currency": {"code": "USD"}}},
                           4545.45),
                          ({"operationAmount": {"amount": "50", "currency": {"code": "AVG"}}},
                           0.00)
                          ])
@patch("requests.get")
def test_transaction_amount(mock_get, test_response, transaction, expected):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = test_response
    mock_get.return_value = mock_response
    result = transaction_amount(transaction)
    assert result == expected


@patch("requests.get")
def test_transaction_amount_not_200(mock_get, test_response, test_transaction_rub):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = test_response
    mock_get.return_value = mock_response
    result = transaction_amount(test_transaction_rub)
    assert result == 0.00


@patch("requests.get")
def test_transaction_amount_read_timeout(mock_get, test_transaction_rub):
    mock_get.side_effect = ReadTimeout
    result = transaction_amount(test_transaction_rub)
    assert result == 0.00
