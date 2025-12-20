from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(type_and_number: str) -> str:
    """Принимает тип и номер каты, возвращает замаскированный номер"""

    card_or_account_number = ""
    for i in type_and_number:
        if i.isdigit():
            card_or_account_number += i

    if len(card_or_account_number) > 16:
        card_number = get_mask_account(int(card_or_account_number))
        return card_number
    else:
        account_number = get_mask_card_number(int(card_or_account_number))
        return account_number
