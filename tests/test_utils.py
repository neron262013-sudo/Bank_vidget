import json
from json import JSONDecodeError

import pytest
from src.utils import get_transactions_data
from unittest.mock import mock_open, patch


@pytest.fixture
def test_data():
    return [
  {
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
]


def test_get_transactions_data(test_data):
    mocked_open = mock_open(read_data=json.dumps(test_data))
    with patch("builtins.open", mocked_open):
        result = get_transactions_data("data/operations.json")
    assert result == test_data

@pytest.mark.parametrize("data, expected", [({"key": 2}, []),
                                            ("str", []),
                                            (2, [])])
def test_get_transactions_data_not_list(data, expected):
    mocked_open = mock_open(read_data=json.dumps(data))
    with patch("builtins.open", mocked_open):
        result = get_transactions_data("data/operations.json")
    assert result == expected

def test_get_transactions_data_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_transactions_data("data/operations.json")
    assert result == []

def test_get_transactions_data_json_decode_error():
    with patch("builtins.open", side_effect=JSONDecodeError("error", "doc", 0)):
        result = get_transactions_data("data/operations.json")
    assert result == []
