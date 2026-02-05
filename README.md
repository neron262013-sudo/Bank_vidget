# Проект "Виджет успешных операций"

## Описание
Это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка

1. Клонируйте репозиторий.
```
git clone https://github.com/neron262013-sudo/Bank_vidget.git
```
2. Установите зависимости.
```
pip install -r requirements.txt
```

## Список зависимостей
- anyio==4.12.1
- argcomplete==3.6.3
- black==25.12.0
- build==1.3.0
- CacheControl==0.14.4
- certifi==2026.1.4
- charset-normalizer==3.4.4
- cleo==2.1.0
- click==8.3.1
- colorama==0.4.6
- coverage==7.13.1
- crashtest==0.4.1
- distlib==0.4.0
- dulwich==0.24.10
- fastjsonschema==2.21.2
- filelock==3.20.2
- findpython==0.7.1
- flake8==7.3.0
- h11==0.16.0
- httpcore==1.0.9
- httpx==0.28.1
- idna==3.11
- iniconfig==2.3.0
- installer==0.7.0
- isort==7.0.0
- jaraco.classes==3.4.0
- jaraco.context==6.0.2
- jaraco.functools==4.4.0
- keyring==25.7.0
- librt==0.7.3
- mccabe==0.7.0
- more-itertools==10.8.0
- msgpack==1.1.2
- mypy==1.19.0
- mypy_extensions==1.1.0
- packaging==25.0
- pathspec==0.12.1
- pbs-installer==2025.12.17
- pipx==1.8.0
- pkginfo==1.12.1.2
- platformdirs==4.5.1
- pluggy==1.6.0
- poetry==2.2.1
- poetry-core==2.2.1
- pycodestyle==2.14.0
- pyflakes==3.4.0
- Pygments==2.19.2
- pyproject_hooks==1.2.0
- pytest==9.0.2
- pytest-cov==7.0.0
- python-dotenv==1.2.1
- pytokens==0.3.0
- pywin32-ctypes==0.2.3
- RapidFuzz==3.14.3
- requests==2.32.5
- requests-toolbelt==1.0.0
- shellingham==1.5.4
- tomlkit==0.13.3
- trove-classifiers==2025.12.1.14
- typing_extensions==4.15.0
- urllib3==2.6.3
- userpath==1.9.2
- virtualenv==20.36.0
- zstandard==0.25.0

## Использование
1. Введите тип и номер карты или счета и получите маску карты или счета. (widget.py)
- Входные параметры str.
- Выходные параметры str.
```
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
```

2. Вспомогательные функции get_mask_card_number и get_mask_account маскируют номер карты и номер аккаунта. (masks.py
- Входные параметры int.
- Выходные параметры str.
```
print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
```

3. Форматирования даты из словаря в дд.мм.гг. (widget.py)
- Входные параметры str.
- Выходные параметры str.
```
print(get_date("2024-03-11T02:26:18.671407"))
```

4. Отфильтровать по статусу. Можно указать аргумент ключа "state". (processing.py)
- Если не указать, то state = "EXECUTED". 
- Входные параметры list[dict], str.
- Выходные параметры list[dict]
```
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                      ))
```

5. Упорядочить по дате. Можно указать аргумент направления по возрастанию или убыванию. (processing.py)
- По умолчанию аргумент направления сортировки = True - убывание. 
- Входные параметры list[dict], bool.
- Выходные параметры list[dict]
```
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
                   ))
```

6. Отфильтровать транзакции из списка словарей по валюте. (generators.py)
- В аргументах нужен список словарей и валюта.
- Входные параметры list[dict], str.
- Выходные параметры Generator[dict, None, None]
``` 
filter_by_currency_gen = filter_by_currency(transactions, "USD")
try:
    while True:
        transaction = next(filter_by_currency_gen)
        print(transaction)
except StopIteration:
    print("Все подходящие транзакции обработаны")
```

7. Описание транзакций. (generators.py)
- В агргументах список словарей.
- Входные параметры list[dict].
- Выходные параметры Generator[str]
```
transaction_descriptions_gen = transaction_descriptions(transactions)
try:
    while True:
        description = next(transaction_descriptions_gen)
        print(description)
except StopIteration:
    print("Все подходящие транзакции обработаны")
```

8. Генератор номеров карт. (generators.py)
- В аргументах начало и конец диапозона.
- Входные параметры int, int. Если нет, то от 1 до 9999999999999999
- Выходные параметры str в формате xxxx xxxx xxxx xxxx
``` 
card_number = card_number_generator()
print(next(card_number))
print(next(card_number))
print(next(card_number))
print(next(card_number))
```

9. Декоратор, который проверяет успешность работы функции. Может вывести тип ошибки и записать в файл, если указать
аргумент. (decorators.py)
- В аргументе указывается название файла. Если не указать, то вывод в консоль.

```
@log()
def my_function(x, y):
    return x + y

my_function(1, 2)
```

10. Форматирует данные о финансовых транзакциях из json файла в python список данных. (utils.py)
- В аргументе путь к файлу с json файлом.
```
print(get_transactions_data("data/operations.json"))
```

11. Возвращает сумму транзакции в рублях из словаря с данными о транзакции. (external_api.py)
- В аргументе словарь с данными о транзакции
- Нужно переименовать файл .env.example в .env и подставить токен с https://apilayer.com/exchangerates_data-api
```
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
```

## Данные для ручных тестов
- Список словарей для filter_by_currency и transaction_descriptions
```
transactions =[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
```

## Тестирование

Тестирование через pytest
1. Установите pytest и pytest-cov
```
poetry add --dev pytest pytest-cov
```
2. Запустите pytest и pytest-cov
```
pytest
pytest -cov
```

## Логирование

Логирование через logging. Логи записываются в файлы в папке logs. Если папки нет - нужно создать в базовой директории.