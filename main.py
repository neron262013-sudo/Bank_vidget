import sys

from src.databases_readers import get_form_xlsx, get_from_csv
from src.utils import get_transactions_data
from src.processing import filter_by_state


def main():
    print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.""")


    counter_file_selection = 0
    counter_status = 0
    filters_counter = 0
    date_order_counter = 0


    while True:
        counter_file_selection += 1
        file_selection = input("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла)
        
Пользователь: """)

        if file_selection == "1":
            print("Выбран JSON-файл")
            selected_file = get_transactions_data("data/operations.json")
            break
        elif file_selection == "2":
            print("Выбран CSV-файл")
            selected_file = get_from_csv("data/transactions.csv")
            break
        elif file_selection == "3":
            print("Выбран XLSX-файл")
            selected_file = get_form_xlsx("data/transactions_excel.xlsx")
            break
        else:
            if counter_file_selection == 5:
                print("Неверное значение.")
                print("Количество вводов превышено. Завершение программы")
                sys.exit()
            print("Неверное значение, попробуйте снова")

    while True:
        counter_status += 1
        status = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    
Пользователь: """)

        if status.upper() == "EXECUTED":
            print("Операции отфильтрованы по статусу \"EXECUTED\"")
            break
        elif status.upper() == "CANCELED":
            print("Операции отфильтрованы по статусу \"CANCELED\"")
            break
        elif status.upper() == "PENDING":
            print("Операции отфильтрованы по статусу \"PENDING\"")
            break
        else:
            if counter_status == 5:
                print(f"Статус операции {status} недоступен.")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print(f"Статус операции {status} недоступен. Попробуйте снова.")

    sort_date_order = None
    filter_word = None
    while True:
        filters_counter += 1
        is_sort_by_date = input("Отсортировать данные по дате? (Да/Нет): ")
        if is_sort_by_date.lower() == "да":
            while True:
                date_order_counter += 1
                sort_date_order = input("Отсортировать по возрастанию или по убыванию?: ")
                if sort_date_order.lower() not in ("по возрастанию", "по убыванию"):
                    if date_order_counter == 5:
                        print("Нужно выбрать \"По возрастанию\" или \"По убыванию\"")
                        print("Количество вводов превышено. Завершение программы.")
                        sys.exit()
                    print("Нужно выбрать \"По возрастанию\" или \"По убыванию\". Попробуйте еще.")
                    continue
                break
        is_only_rub = input("Выводить только рублевые транзакции? (Да/Нет): ")
        is_filter_str = input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ")
        if is_filter_str.lower() == "да":
            filter_word = input("Введите слово для фильтрации: ")
        if (is_sort_by_date.lower() not in ("да", "нет") or
                is_only_rub.lower() not in ("да", "нет") or
                is_filter_str.lower() not in ("да", "нет")):

            if filters_counter == 5:
                print("Выбрать можно только Да или Нет.")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print("Выбрать можно только Да или Нет. Попробуйте снова")
            continue
        break

    print("Распечатываю итоговый список транзакций...")

    # filtered_operations_by_state = filter_by_state(selected_file)
    #
    # if is_sort_by_date.lower() == "да":





if __name__ == "__main__":
    main()
