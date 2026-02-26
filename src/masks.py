import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{BASE_DIR}/logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s:%(filename)s:%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает ее замаскированную маску"""

    logger.info("Начало работы функции get_mask_card_number")
    # Проверка, что в номере 16 символов
    if not len(str(card_number)) == 16:
        logger.error(f"Не правильный формат номера карты: {card_number}")
        raise ValueError("Не правильный формат номера карты")

    # Проверка, что значение int
    # if not isinstance(card_number, int):
    #     logger.error(f"Не правильный формат номера карты {card_number}")
    #     raise ValueError("Не правильный формат номера карты")

    logger.info("Маскировка номера карты и завершение работы функции get_mask_card_number")
    # Маскировка номера карты
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его замаскированную маску"""

    logger.info("Начало работы функции get_mask_account")
    # Проверка, что в номере 20 символов
    if not len(str(account_number)) == 20:
        logger.error(f"Не правильный формат номера счета: {account_number}")
        raise ValueError("Не правильный формат номера счета")

    # Проверка, что формат int
    # if not isinstance(account_number, int):
    #     logger.error(f"Не правильный формат номера счета: {account_number}")
    #     raise ValueError("Не правильный формат номера счета")

    # Маскирует номер счета
    logger.info("Маскировка номера карты и завершение работы функции get_mask_account")
    return f"**{str(account_number)[-4:]}"

