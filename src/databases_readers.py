import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_from_csv(path: pd.DataFrame) -> list[dict]:
    """ Считывает данные из csv файлов """

    data = pd.read_csv(BASE_DIR / path)
    return data.to_dict(orient="records")


def get_form_xlsx(path: pd.DataFrame) -> list[dict]:
    """ Считывает данные из xlsx файлов """

    data = pd.read_excel(BASE_DIR / path)
    return data.to_dict(orient="records")

print(get_form_xlsx("data/transactions_excel.xlsx"))