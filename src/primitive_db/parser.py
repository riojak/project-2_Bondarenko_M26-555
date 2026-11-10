def read_conditions(condition):
    '''Принимает условие от пользователя в строковом виде
    формата 'key = value' - для int и bool
    формата 'key = "value"' - для str.
    Преобразует и отдает словарь 
    формата {key: value} - для int и bool
    формата {key: "value"} - для str
    Проверяет на типы и на одинаковые кавычки для строк
    При неправильных кавычках возвращает None
    '''


    parts = condition.split("=")
    if len(parts) != 2:
        print('Ошибка: Ввод значений должен идти через "=".')
        return
    column = parts[0].strip()
    if column == "":
        print("Ошибка: Название столбца не может быть пустым.")
        return
    values = parts[1].strip()
    if values.removeprefix("-").isdigit():
        values = int(values)
    elif values.lower() == "true":
        values = True
    elif values.lower() == "false":
        values = False
    else:
        if len(values) >= 2:
            if (
                values.startswith('"') and values.endswith('"')
                or values.startswith("'") and values.endswith("'")
            ):
                values = values[1:-1]
            else:
                print("Ошибка: Кавычки должны быть одинаковыми с двух сторон.")
                return
        else:
            print("Ошибка: Кавычки должны быть одинаковыми с двух сторон.")
            return
    return {column: values}

def read_values(values_str):
    values_list = values_str.split(",")
    clean_values = []
    for value in values_list:
        value = value.strip()
        clean_values.append(value)
    result = []
    for value in clean_values:
        if value.removeprefix("-").isdigit():
            value = int(value)
        elif value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False
        else:
            if len(value) >= 2:
                if (
                    value.startswith('"') and value.endswith('"')
                    or value.startswith("'") and value.endswith("'")
                ):
                    value = value[1:-1]
                else:
                    print("Ошибка: Кавычки должны быть одинаковыми с двух сторон.")
                    return
            else:
                print("Ошибка: Кавычки должны быть одинаковыми с двух сторон.")
                return
        result.append(value)
    return result