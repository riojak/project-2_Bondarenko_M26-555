import prompt


def welcome():
    print("Первая попытка запустить проект!")
    print()
    print("***")
    help_func()
    while True:
        command = prompt.string("Введите команду: ")
        if command == "exit":
            break
        elif command == "help":
            help_func()

def help_func():
    print("<command> exit - выйти из программы")
    print("<command> help - справочная информация")
    