from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


def get_from_csv(path: str) -> list[dict]:
    """ Считывает данные из csv файлов и возвращаем список словарей с данными """

    # Проверяем, что путь указан верно
    if "data" not in path or "csv" not in path:
        raise ValueError(f"Путь должен быть 'data/file_name.csv', а передан {path}")

    full_path = BASE_DIR / path

    # Проверяем, что файл существует в указанной директории
    if not full_path.exists():
        raise ValueError(f"Файл не существует по пути {full_path}")

    # Читаем из csv и формируем словарь с данными
    data = pd.read_csv(full_path)
    return data.to_dict(orient="records")


def get_form_xlsx(path: str) -> list[dict]:
    """ Считывает данные из xlsx файлов и возвращаем список словарей с данными """

    # Проверяем, что путь указан верно
    if "data" not in path or "xlsx" not in path:
        raise ValueError(f"Путь должен быть 'data/file_name.xlsx', а передан {path}")

    full_path = BASE_DIR / path

    # Проверяем, что файл существует в указанной директории
    if not full_path.exists():
        raise ValueError(f"Файл не существует по пути {full_path}")

    # Читаем из xlsx и формируем словарь с данными
    data = pd.read_excel(full_path)
    return data.to_dict(orient="records")
