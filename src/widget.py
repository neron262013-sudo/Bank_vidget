import re

from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Принимает тип и номер карты или счета, возвращает маску"""

    # Проверка, что формат - строка
    if not isinstance(type_and_number, str):
        raise AttributeError("Не правильный формат данных")


    # Удаляет все буквы и оставляет только номер карты или аккаунта
    card_or_account_number = ""
    for simbol in type_and_number:
        if simbol.isdigit():
            card_or_account_number += simbol


    # Проверяет длинну введенных номеров
    if len(card_or_account_number) not in (16, 20):
        raise ValueError("Не правильная длинна номера")


    # Номер карты = 16 символов. Если больше, то это номер аккаунта. Маскируем соответственно из файла masks.
    if len(card_or_account_number) > 16:
        card_number = get_mask_account(int(card_or_account_number))
        return card_number
    else:
        account_number = get_mask_card_number(int(card_or_account_number))
        return account_number


def get_date(raw_date: str) -> str:
    """Принимает сырую дату и возвращает в формате ДД.ММ.ГГГГ"""

    # Проверка что формат str
    if not isinstance(raw_date, str):
        raise TypeError("Не правлиьный тип данных")


    # Проверка формата даты по образцу "2024-03-11T02:26:18.671407"
    if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+$", raw_date):
        raise ValueError("Не правильный формат даты")


    # Форматируем дату просто через срезы.
    formatted_date = raw_date[8:10], raw_date[5:7], raw_date[:4]
    return ".".join(formatted_date)
