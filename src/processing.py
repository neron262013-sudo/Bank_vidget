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

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
            {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'}]
                   , False))

#[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
# {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'}]

# [{'id': 615064591, 'state': 'SOME_TEXT', 'date': '2018-05-14T08:21:33.419441'},
# {'id': 615064591, 'state': 'ANOTHER_TEXT', 'date': '2018-05-14T08:21:33.419441'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
