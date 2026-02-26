import sys

from src.databases_readers import get_form_xlsx, get_from_csv
from src.utils import get_transactions_data
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.widget import get_date, mask_account_card


def main():
    print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.""")


    counter_file_selection = 0
    counter_status = 0
    filters_counter = 0
    date_order_counter = 0
    only_rub_counter = 0
    filter_str_counter = 0


    while True:
        counter_file_selection += 1
        file_selection = input("""Выберите необходимый пункт меню:\n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла)
        
Пользователь: """)
        if file_selection == "1":
            print("\nВыбран JSON-файл")
            selected_file = get_transactions_data("data/operations.json")
            break
        elif file_selection == "2":
            print("\nВыбран CSV-файл")
            selected_file = get_from_csv("data/transactions.csv")
            break
        elif file_selection == "3":
            print("\nВыбран XLSX-файл")
            selected_file = get_form_xlsx("data/transactions_excel.xlsx")
            break
        else:
            if counter_file_selection == 5:
                print("\nНеверное значение.")
                print("Количество вводов превышено. Завершение программы")
                sys.exit()
            print("\nНеверное значение, попробуйте снова")

    while True:
        counter_status += 1
        status = input("""\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    
Пользователь: """)

        if status.upper() == "EXECUTED":
            print("\nОперации отфильтрованы по статусу \"EXECUTED\"")
            break
        elif status.upper() == "CANCELED":
            print("\nОперации отфильтрованы по статусу \"CANCELED\"")
            break
        elif status.upper() == "PENDING":
            print("\nОперации отфильтрованы по статусу \"PENDING\"")
            break
        else:
            if counter_status == 5:
                print(f"\nСтатус операции {status} недоступен.")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print(f"\nСтатус операции {status} недоступен. Попробуйте снова.")

    while True:
        filters_counter += 1
        is_sort_by_date = input("\nОтсортировать данные по дате? (Да/Нет): ")
        if is_sort_by_date.lower() not in ["да", "нет"]:
            if filters_counter == 5:
                print(f"\nНужно указать \"Да\" или \"Нет\"")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print(f"\nНужно указать \"Да\" или \"Нет\". Попробуйте снова.")
            continue
        break

    if is_sort_by_date.lower() == "да":
        while True:
            date_order_counter += 1
            sort_date_order = input("\nОтсортировать по возрастанию или по убыванию?: ")
            if sort_date_order.lower() not in ["по возрастанию", "по убыванию"]:
                if date_order_counter == 5:
                    print(f"\nНужно указать По возрастанию или По убыванию")
                    print("Количество вводов превышено. Завершение программы.")
                    sys.exit()
                print(f"\nНужно указать По возрастанию или По убыванию. Попробуйте снова")
                continue
            break

    while True:
        only_rub_counter += 1
        is_only_rub = input("\nВыводить только рублевые транзакции? (Да/Нет): ")
        if is_only_rub.lower() not in ["да", "нет"]:
            if only_rub_counter == 5:
                print(f"\nНужно указать \"Да\" или \"Нет\"")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print(f"\nНужно указать \"Да\" или \"Нет\". Попробуйте снова.")
            continue
        break

    while True:
        filter_str_counter += 1
        is_filter_str = input("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ")
        if is_filter_str.lower() not in ["да", "нет"]:
            if filter_str_counter == 5:
                print(f"\nНужно указать \"Да\" или \"Нет\"")
                print("Количество вводов превышено. Завершение программы.")
                sys.exit()
            print(f"\nНужно указать \"Да\" или \"Нет\". Попробуйте снова.")
            continue
        break

    if is_filter_str.lower() == "да":
        filter_word = input("\nВведите слово для фильтрации: ")


    print("\nРаспечатываю итоговый список транзакций...")

    final_list_of_transactions = filter_by_state(selected_file, status.upper())
    if is_sort_by_date.lower() == "да":
        if sort_date_order.lower() == "по возрастанию":
            final_list_of_transactions = sort_by_date(final_list_of_transactions, False)
        else:
            final_list_of_transactions = sort_by_date(final_list_of_transactions)
    if is_only_rub.lower() == "да":
        final_list_of_transactions = process_bank_search(final_list_of_transactions, "RUB")
    if is_filter_str.lower() == "да":
        final_list_of_transactions = process_bank_search(final_list_of_transactions, filter_word)


    if not final_list_of_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(final_list_of_transactions)}")
        for transaction in final_list_of_transactions:
            final_transaction = list()
            final_transaction.append(f"{get_date(transaction['date'])} {transaction['description']}")
            if "Перевод" not in transaction["description"]:
                transaction_to = transaction.get("to")
                final_transaction.append(mask_account_card(transaction_to))
            else:
                transaction_from = transaction.get("from")
                transaction_to = transaction.get("to")
                final_transaction.append(f"{mask_account_card(str(transaction_from))} -> "
                                         f"{mask_account_card(str(transaction_to))}")
            final_transaction.append(f"Сумма: {transaction['operationAmount']['amount']}")
            print("\n".join(final_transaction))
            print()









if __name__ == "__main__":
    main()
