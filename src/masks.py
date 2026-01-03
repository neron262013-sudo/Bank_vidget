def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее замаскированную маску"""

    if not len(str(card_number)) == 16:
        raise ValueError("Не правильный формат номера карты")

    if not isinstance(card_number, int):
        raise ValueError("Не правильный формат номера карты")

    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его замаскированную маску"""

    if not len(str(account_number)) == 20:
        raise ValueError("Не правильный формат номера счета")

    if not isinstance(account_number, int):
        raise ValueError("Не правильный формат номера карты")

    return f"**{str(account_number)[-4:]}"
