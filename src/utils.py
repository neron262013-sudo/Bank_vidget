import json
from json import JSONDecodeError
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def get_transactions_data(path: str) -> list:
    """ Список данных о финансовых транзакциях """

    # Обрабатываем исключения.
    try:
        # Если все ок, то открываем файл и преобразуем в Python объект.
        with open(f"{BASE_DIR}/{path}", encoding="utf-8") as data:
            transactions_data = json.load(data)

            # Проверяем, что объект - список
            if not isinstance(transactions_data, list):
                return []

    # Если файла нет по пути или есть ошибки в файле, то выводим пустой список.
    except (FileNotFoundError, JSONDecodeError):
        return []

    return transactions_data



print(get_transactions_data("data/operations.json"))
