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
