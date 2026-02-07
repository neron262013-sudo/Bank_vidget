import json
import logging
from json import JSONDecodeError
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{BASE_DIR}/logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_data(path: str) -> list:
    """ Форматируем данные об операциях из json в python список данных о финансовых транзакциях """

    logger.info("Начало работы функции get_transactions_data")
    # Обрабатываем исключения.
    try:
        logger.info(f"Открытие файла {path}")
        # Если все ок, то открываем файл и преобразуем в Python объект.
        with open(f"{BASE_DIR}/{path}", encoding="utf-8") as data:
            transactions_data = json.load(data)
            logger.info(f"Файл {path} открыть удалось, операции отформатированы")
        # Проверяем, что объект - список
        if not isinstance(transactions_data, list):
            logger.error("Объект не список")
            return []

    # Если файла нет по пути или есть ошибки в файле, то выводим пустой список.
    except (FileNotFoundError, JSONDecodeError):
        logger.error(f"Не удалось открыть файл {path}")
        return []
    logger.info("Конец работы функции get_transactions_data")
    return transactions_data
