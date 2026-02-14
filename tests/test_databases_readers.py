from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

from src.databases_readers import get_form_xlsx, get_from_csv

BASE_DIR = Path(__file__).resolve().parent.parent


@pytest.fixture
def test_data_base():
    sample_dict = {"id": 650703, "state": "EXECUTED"}
    return pd.DataFrame([sample_dict])


# Тесты для csv
@patch("src.databases_readers.pd.read_csv")
@patch("src.databases_readers.Path.exists")
def test_get_from_csv(mock_exists, mock_read_csv, test_data_base):
    mock_exists.return_value = True
    mock_read_csv.return_value = test_data_base
    result = get_from_csv("data/path.csv")
    assert result == [{"id": 650703, "state": "EXECUTED"}]


@pytest.mark.parametrize("wrong_path, expected",
                         [
                             ("path.csv", "Путь должен быть 'data/file_name.csv', а передан path.csv"),
                             ("data/path", "Путь должен быть 'data/file_name.csv', а передан data/path")])
@patch("src.databases_readers.pd.read_csv")
def test_get_from_csv_no_data_in_path(mock_read_csv, test_data_base, wrong_path, expected):
    mock_read_csv.return_value = test_data_base
    with pytest.raises(ValueError) as exception_info:
        get_from_csv(wrong_path)
    assert str(exception_info.value) == expected


def test_get_from_csv_file_not_find():
    non_existing_file_in_path = "data/not_exist_file.csv"
    full_path = BASE_DIR / non_existing_file_in_path
    with pytest.raises(ValueError) as exception_info:
        get_from_csv(non_existing_file_in_path)
    assert str(exception_info.value) == f"Файл не существует по пути {full_path}"


# # Тесты для xlsx
@patch("src.databases_readers.pd.read_excel")
@patch("src.databases_readers.Path.exists")
def test_get_from_xlsx(mock_exists, mock_read_csv, test_data_base):
    mock_exists.return_value = True
    mock_read_csv.return_value = test_data_base
    result = get_form_xlsx("data/path.xlsx")
    assert result == [{"id": 650703, "state": "EXECUTED"}]


@pytest.mark.parametrize("wrong_path, expected",
                         [
                             ("path.xlsx", "Путь должен быть 'data/file_name.xlsx', а передан path.xlsx"),
                             ("data/path", "Путь должен быть 'data/file_name.xlsx', а передан data/path")])
@patch("src.databases_readers.pd.read_excel")
def test_get_from_xlsx_no_data_in_path(mock_read_csv, test_data_base, wrong_path, expected):
    mock_read_csv.return_value = test_data_base
    with pytest.raises(ValueError) as exception_info:
        get_form_xlsx(wrong_path)
    assert str(exception_info.value) == expected


def test_get_from_xlsx_file_not_find():
    non_existing_file_in_path = "data/not_exist_file.xlsx"
    full_path = BASE_DIR / non_existing_file_in_path
    with pytest.raises(ValueError) as exception_info:
        get_form_xlsx(non_existing_file_in_path)
    assert str(exception_info.value) == f"Файл не существует по пути {full_path}"
