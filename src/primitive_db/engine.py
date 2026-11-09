import shlex

import prompt

from primitive_db.core import create_table, drop_table
from primitive_db.utils import load_metadata, save_metadata


def run():
    help_func()
    while True:
        metadata = load_metadata("db_meta.json")
        user_input = prompt.string("Введите команду: ")
        args = shlex.split(user_input)
        if args == []:
            continue
        action = args[0]
        if action == "exit":
            break
        elif action == "help":
            help_func()
        elif action == "create_table":
            if len(args) < 3:
                print("Ошибка: Не введено имя таблицы или хотя бы один столбец.")
                continue
            table_name = args[1]
            columns = args[2:]
            result = create_table(metadata, table_name, columns)
            if result is not None:
                save_metadata("db_meta.json", result)
        elif action == "drop_table":
            if len(args) != 2:
                print("Ошибка: Для удаления таблицы необходимо только имя.")
                continue
            table_name = args[1]
            result = drop_table(metadata, table_name)
            if result is not None:
                save_metadata("db_meta.json", result)
        elif action == "list_tables":
            if metadata == {}:
                print("Таблиц пока нет.")
                continue
            for name in metadata:
                print(f"{name}")
        else:
            print(f"Функции {action} нет. Попробуйте снова.")


def help_func():
    print("\n***Процесс работы с таблицей***\n")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("Доступные типы столбцов: int, str, bool")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")

    print("\nОбщие команды:")
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация\n")
    