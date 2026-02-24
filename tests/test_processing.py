import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.fixture()
def list_of_dicts():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
            {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'}]


@pytest.fixture()
def sorted_list_of_dict_by_decreasing():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
            {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'}]


@pytest.fixture()
def sorted_list_of_dict_by_increasing():
    return [{'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
            {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture()
def transactions_data_description():
    return [{"description": "Перевод организации"},
            {"description": "Перевод организации"},
            {"description": "Перевод со счета на счет"},
            {"description": "Перевод с карты на карту"}]


@pytest.fixture()
def categories_data():
    return ["перевод организации", "перевод со счета на счет"]


def test_filter_by_state(list_of_dicts):
    assert (filter_by_state(list_of_dicts, "CANCELED")) == \
           [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state_no_state(list_of_dicts):
    assert (filter_by_state(list_of_dicts)) == \
           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("state", ["SOME_TEXT",
                                   "ANOTHER_TEXT",
                                   "executed",
                                   "canceled"])
def test_filter_by_state_state_values(list_of_dicts, state):
    with pytest.raises(ValueError):
        filter_by_state(list_of_dicts, state)


def test_sort_by_date(list_of_dicts, sorted_list_of_dict_by_decreasing):
    assert sort_by_date(list_of_dicts) == sorted_list_of_dict_by_decreasing


def test_sort_by_date_decreasing(list_of_dicts, sorted_list_of_dict_by_decreasing):
    assert sort_by_date(list_of_dicts, True) == sorted_list_of_dict_by_decreasing


def test_sort_by_date_increasing(list_of_dicts, sorted_list_of_dict_by_increasing):
    assert sort_by_date(list_of_dicts, False) == sorted_list_of_dict_by_increasing


@pytest.mark.parametrize("search, expected",
                         [("EXECUTED",
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ("CanceleD",
                           [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                          ("Not found",
                           [])
                          ]
                         )
def test_process_bank_search(search, expected, list_of_dicts):
    assert process_bank_search(list_of_dicts, search) == expected


@pytest.mark.parametrize("search", [123, [], {}, ()])
def test_process_bank_search_wrong_search(search, list_of_dicts):
    with pytest.raises(TypeError) as exception:
        process_bank_search(list_of_dicts, search)
    assert str(exception.value) == "Параметр поиска должен быть типом str"


@pytest.mark.parametrize("data", ["text", 123, {}, (), ["text", "text_1"], [1, 2]])
def test_process_bank_search_wrong_data(data):
    with pytest.raises(TypeError) as exception:
        process_bank_search(data, "search")
    assert str(exception.value) == "Параметр данных должен быть list[dict]"


def test_process_bank_operations(transactions_data_description, categories_data):
    assert process_bank_operations(transactions_data_description, categories_data) == {"перевод организации": 2,
                                                                                       "перевод со счета на счет": 1}


@pytest.mark.parametrize("categories", [[1, 2], [{"1": 1}, {"2": 2}, 1, "text", (1, 2, 3), {"1": 1}]])
def test_process_bank_operations_wrong_categories(transactions_data_description, categories):
    with pytest.raises(TypeError) as exception:
        process_bank_operations(transactions_data_description, categories)
    assert str(exception.value) == "Параметр категорий должен быть списком c str данными"


@pytest.mark.parametrize("data", ["text", 123, {}, (), ["text", "text_1"], [1, 2]])
def test_process_bank_operations_wrong_data(data, categories_data):
    with pytest.raises(TypeError) as exception:
        process_bank_operations(data, categories_data)
    assert str(exception.value) == "Параметр данных должен быть list[dict]"
