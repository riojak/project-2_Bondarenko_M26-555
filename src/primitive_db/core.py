def create_table(metadata, table_name, columns):
    if table_name in metadata:
        print(f'Ошибка: Таблица "{table_name}" уже существует.')
        return
    allowed_types = ("int", "str", "bool")
    for column in columns:
        parts = column.split(":")
        data_type = parts[1]
        if data_type not in allowed_types:
            print(f'Ошибка: Указанный тип "{data_type}" не поддерживается.')
            return
    columns.insert(0, "ID:int")
    metadata[table_name] = columns
    return metadata

def drop_table(metadata, table_name):
    if table_name not in metadata:
        print(f'Ошибка: Таблица "{table_name}" не существует.')
        return
    del metadata[table_name]
    return metadata