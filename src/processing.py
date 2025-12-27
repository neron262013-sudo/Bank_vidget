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

def sort_by_date(list_of_data_dicts: list[dict], sort_order: str = "убывание") -> list[dict]:
    """Сортирует словари в списке по дате. Можно указать порядок сортировки. Убывание по умолчанию"""

    # Проверяет что введено в sort_order. Если ничего или "убывание", то сортировка по убыванию.
    # Иначе - по возрастанию.
    order = False
    if sort_order == "убывание":
        order = True

    # Возвращаем отсортированный по дате список словарей
    return sorted(list_of_data_dicts, key=lambda x: x["date"], reverse=order)
