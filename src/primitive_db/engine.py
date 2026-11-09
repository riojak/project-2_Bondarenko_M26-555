import prompt
import shlex
from primitive_db.core import create_table
from primitive_db.core import drop_table
from primitive_db.utils import load_metadata
from primitive_db.utils import save_metadata


def run():
    print("Первая попытка запустить проект!")
    print()
    print("***")
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


def help_func():
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")
    