from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Принимает тип и номер карты или счета, возвращает маску"""

    # Удаляет все буквы и оставляет только номер карты или аккаунта
    card_or_account_number = ""
    for simbol in type_and_number:
        if simbol.isdigit():
            card_or_account_number += simbol

    # Номер карты = 16 символов. Если больше, то это номер аккаунта. Маскируем соответственно из файла masks.
    if len(card_or_account_number) > 16:
        card_number = get_mask_account(int(card_or_account_number))
        return card_number
    else:
        account_number = get_mask_card_number(int(card_or_account_number))
        return account_number


def get_date(raw_date: str) -> str:
    """Принимает сырую дату и возвращает в формате ДД.ММ.ГГГГ"""

    # Форматируем дату просто через срезы.
    formatted_date = raw_date[8:10], raw_date[5:7], raw_date[:4]
    return ".".join(formatted_date)
