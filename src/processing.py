import re
from collections import Counter


def filter_by_state(list_of_data_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей с данными по параметру state"""

    # Проверка, что в состояние счета введены определенные параметры
    if state not in ("EXECUTED", "CANCELED", "PENDING"):
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


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Поиск строки в списке словарей с операциями"""

    # Проверяем, что в data ввели список словарей
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise TypeError("Параметр данных должен быть list[dict]")

    # Проверяем, что в search ввели строку
    if not isinstance(search, str):
        raise TypeError("Параметр поиска должен быть типом str")

    pattern = re.compile(search, re.IGNORECASE)
    result_list = list()
    for operation in data:
        for value in operation.values():
            if pattern.search(str(value)):
                result_list.append(operation)
    return result_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций по типу из данных по операциям"""

    # Проверяем, что в data ввели список словарей
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise TypeError("Параметр данных должен быть list[dict]")

    # Проверяем, что в categories ввели список со строками
    if not isinstance(categories, list) or not all(isinstance(item, str) for item in categories):
        raise TypeError("Параметр категорий должен быть списком c str данными")

    operations_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            pattern = re.compile(category, re.IGNORECASE)
            if pattern.search(description):
                operations_counter[category] += 1
    return dict(operations_counter)
