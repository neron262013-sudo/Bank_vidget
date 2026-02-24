import re
from collections import defaultdict


def filter_by_state(list_of_data_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей с данными по параметру state"""

    # Проверка, что в состояние счета введены определенные параметры
    if state not in ("EXECUTED", "CANCELED"):
        raise ValueError("Не верное значение состояния счета")

    # Проходим по словарям в списке. Проверяем, есть ли ключ "state" через .get.
    # Заносим все словари с указанным "state" в новый словарь и возвращаем.
    new_list_of_data_dicts = []
    for data_dict in list_of_data_dicts:
        data_state = data_dict.get("state")
        if data_state == state:
            new_list_of_data_dicts.append(data_dict)

    return new_list_of_data_dicts


def sort_by_date(list_of_data_dicts: list[dict], sort_order: bool = True) -> list[dict]:
    """Сортирует словари в списке по дате. Можно указать порядок сортировки. Убывание по умолчанию"""

    # Возвращаем отсортированный по дате список словарей
    return sorted(list_of_data_dicts, key=lambda x: x["date"], reverse=sort_order)


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка."""


    pattern = re.compile(str(search), re.IGNORECASE)
    result_list = list()
    for operation in data:
        for value in operation.values():
            if pattern.search(str(value)):
                result_list.append(operation)
    return result_list


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    operations_counter = defaultdict(int)
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            pattern = re.compile(category, re.IGNORECASE)
            if pattern.search(description):
                operations_counter[category] += 1
    return dict(operations_counter)




# print(process_bank_search([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "EXECUTED"))

# print(process_bank_operations([
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     }], ["перевод организации", "перевод со счета на счет"]))
