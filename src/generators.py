from typing import Generator
import random

def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator[dict, None, None]:
    """Принимает список транзакций.
    Возвращает генератор, который выдает транзакции, где валюта операции соответствует заданной."""

    if transactions_list:
        for transaction in transactions_list:
            # Проверка, что в словаре есть нужные ключи и они не пусты.
            code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

            # Если значение code = указанной валюте, то возвращаем генератор со словарем.
            if code == currency:
                yield transaction
            else:
                yield "Нет указанной валюты"
    else:
        yield "Список транзакций пуст"

def transaction_descriptions(transactions_list: list[dict]) -> Generator[str]:
    """Принимает список транзакций. Возвращает генератор с описанием транзакции"""

    if transactions_list:
        for transaction in transactions_list:
            # Проверяем, что ключ desctiption есть в словаре  возвращаем генератор с описанием транзакции.
            description = transaction.get("description")
            yield description
    else:
        yield "Список транзакций пуст"

# Собираем все номера карт во множество, чтобы не повторяться
set_of_card_numbers = set()
def card_number_generator(start: int = 1, end: int = 9999999999999999) -> str:
    """Генератор номеров карт в формате xxxx xxxx xxxx xxxx"""

    while True:
        # Генерируем номер. Если длинна меньше 16, то дозаполним нулями в начало
        new_card_number = str(random.randint(start, end)).zfill(16)

        # Проверка, что номер не повторяется
        if not new_card_number in set_of_card_numbers:
            set_of_card_numbers.add(new_card_number)
            formated_card_number = (f"{new_card_number[0:4]} {new_card_number[4:8]} "
                                    f"{new_card_number[8:12]} {new_card_number[12:]}")
            yield formated_card_number
        else:
            yield "Номера в указанном диапазоне закончились"


card_number = card_number_generator()
print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))