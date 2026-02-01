import requests
from dotenv import load_dotenv
import os

from requests import ReadTimeout


def transaction_amount(transaction: dict) -> float:
    """ Возвращает сумму транзакции в рублях """

    # Грузим конфиденциальные данные из .env
    load_dotenv()

    # Делаем запрос с использованием токена
    exchangerates_token = os.getenv("EXCHANGE_RATES_TOKEN")
    headers = {"apikey": exchangerates_token}
    url = "https://api.apilayer.com/exchangerates_data/latest"

    try:
        response = requests.get(url, headers=headers, timeout=10)
    except ReadTimeout:
        return 0.00

    # Проверка на ответ
    if response.status_code != 200:
        return 0.00

    # Объявляем курсы валют
    exchange_rates = response.json()
    eur_usd_exchange_rate = float(exchange_rates["rates"]["USD"])
    eur_rub_exchange_rate = float(exchange_rates["rates"]["RUB"])
    usd_rub_exchange_rate = float(eur_rub_exchange_rate / eur_usd_exchange_rate)

    operation_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    operation_amount = float(transaction.get("operationAmount", {}).get("amount"))

    # Получаем сумму транзакции в рублях
    if operation_code == "USD":
        amount = round(operation_amount * usd_rub_exchange_rate, 2)
    elif operation_code == "EUR":
        amount = round(operation_amount * eur_rub_exchange_rate, 2)
    elif operation_code == "RUB":
        amount = round(operation_amount, 2)
    else:
        return 0.00
    return amount




print(transaction_amount({
"id": 441945886,
"state": "EXECUTED",
"date": "2019-08-26T10:50:58.294041",
"operationAmount": {
  "amount": "31957.58",
  "currency": {
    "name": "руб.",
    "code": "RUB"
  }
},
"description": "Перевод организации",
"from": "Maestro 1596837868705199",
"to": "Счет 64686473678894779589"
}))
