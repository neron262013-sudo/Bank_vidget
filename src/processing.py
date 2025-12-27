def filter_by_state(list_of_data_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей с данными по параметру state"""

    # Проходим по словарям в списке. Проверяем, есть ли ключ "state" через .get.
    # Заносим все словари с указанным "state" в новый словарь и возвращаем.
    new_list_of_data_dicts = []
    for i in list_of_data_dicts:
        data_state = i.get("state")
        if data_state == state:
            new_list_of_data_dicts.append(i)

    return new_list_of_data_dicts