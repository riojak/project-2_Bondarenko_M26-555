def create_table(metadata, table_name, columns):
    if table_name in metadata:
        print(f'Ошибка: Таблица "{table_name}" уже существует.')
        return
    allowed_types = ("int", "str", "bool")
    id_exists = False
    for column in columns:
        parts = column.split(":")
        if len(parts)!= 2 or "" in parts:
            print("Ошибка: Не указан тип или название столбца.")
            return
        if parts[0] == "ID":
            id_exists = True
        if parts[0] == "ID" and parts[1] != "int":
            print('Ошибка: ID может быть только "int"')
            return
        data_type = parts[1]
        if data_type not in allowed_types:
            print(f'Ошибка: Указанный тип "{data_type}" не поддерживается.')
            return
    if not id_exists:
        columns.insert(0, "ID:int")
    metadata[table_name] = columns
    return metadata

def drop_table(metadata, table_name):
    if table_name not in metadata:
        print(f'Ошибка: Таблица "{table_name}" не существует.')
        return
    del metadata[table_name]
    return metadata