def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее замаскированную маску"""

    # Проверка, что в номере 16 символов
    if not len(str(card_number)) == 16:
        raise ValueError("Не правильный формат номера карты")

    # Проверка, что значение int
    if not isinstance(card_number, int):
        raise ValueError("Не правильный формат номера карты")

    # Маскировка номера карты
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его замаскированную маску"""

    # Проверка, что в номере 20 символов
    if not len(str(account_number)) == 20:
        raise ValueError("Не правильный формат номера счета")

    # Проверка, что формат int
    if not isinstance(account_number, int):
        raise ValueError("Не правильный формат номера карты")

    # Маскирует номер счета
    return f"**{str(account_number)[-4:]}"
