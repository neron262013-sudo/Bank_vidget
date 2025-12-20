def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее замаскированную маску"""

    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его замаскированную маску"""

    return f"**{str(account_number)[-4:]}"
