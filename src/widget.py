import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Принимает тип и номер карты или счета, возвращает маску"""

    # Проверка, что формат - строка
    if not isinstance(type_and_number, str):
        raise AttributeError("Не правильный формат данных")

    # Удаляет все буквы и оставляет только номер карты или аккаунта
    card_or_account_number = ""
    for symbol in type_and_number:
        if symbol.isdigit():
            card_or_account_number += symbol

    # Удаляет все цифры и оставляет буквы
    type_of_card_or_account = ""
    for symbol in type_and_number:
        if symbol.isalpha():
            type_of_card_or_account += symbol

    # Проверяет длинну введенных номеров
    if len(card_or_account_number) not in (16, 20):
        raise ValueError("Не правильная длинна номера")

    # Номер карты = 16 символов. Если больше, то это номер аккаунта. Маскируем соответственно из файла masks.
    if len(card_or_account_number) > 16:
        card_number = get_mask_account(card_or_account_number)
        return str(f"{type_of_card_or_account} {card_number}")
    else:
        account_number = get_mask_card_number(card_or_account_number)
        return str(f"{type_of_card_or_account} {account_number}")


def get_date(raw_date: str) -> str:
    """Принимает сырую дату и возвращает в формате ДД.ММ.ГГГГ"""

    # Проверка, что формат str
    if not isinstance(raw_date, str):
        raise TypeError("Не правильный тип данных")

    # Проверка формата даты по образцу "2024-03-11T02:26:18.671407"
    if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", raw_date):
        raise ValueError("Не правильный формат даты")

    # Форматируем дату просто через срезы.
    formatted_date = raw_date[8:10], raw_date[5:7], raw_date[:4]
    return ".".join(formatted_date)
