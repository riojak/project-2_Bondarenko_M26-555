from primitive_db.utils import load_table_data


def create_table(metadata, table_name, columns):
    if table_name in metadata:
        print(f'Ошибка: Таблица "{table_name}" уже существует.')
        return
    allowed_types = ("int", "str", "bool")
    id_exists = False
    for column in columns:
        parts = column.split(":")
        if len(parts) != 2 or "" in parts:
            print(f'Некорректное значение: {column}. Попробуйте снова.')
            return
        if parts[0] == "ID":
            id_exists = True
        if parts[0] == "ID" and parts[1] != "int":
            print(f'Некорректное значение: {column}. Попробуйте снова.')
            return
        data_type = parts[1]
        if data_type not in allowed_types:
            print(f'Некорректное значение: {data_type}. Попробуйте снова.')
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

def insert(metadata, table_name, values):
    if table_name not in metadata:
        print(f'Ошибка: Таблица "{table_name}" не существует.')
        return
    if len(values) != (len(metadata[table_name]) - 1):
        print("Ошибка: Количество значений должно быть равно количеству столбцов.")
        return
    for value, column in zip(values, metadata[table_name][1:]):
        parts = column.split(":")
        if parts[1] == "str" and type(value) is not str:
            print("Ошибка: Некорректный тип данных.")
            return
        if parts[1] == "int" and type(value) is not int:
            print("Ошибка: Некорректный тип данных.")
            return
        if parts[1] == "bool" and type(value) is not bool:
            print("Ошибка: Некорректный тип данных.")
            return
    table_data = load_table_data(table_name)
    if table_data == []:
        new_id = 1
    else:
        new_id = max(row["ID"] for row in table_data) + 1
    new_row = {"ID": new_id}
    for value, column in zip(values, metadata[table_name][1:]):
        parts = column.split(":")
        new_row[parts[0]] = value
    table_data.append(new_row)
    return table_data

def select(table_data, where_clause=None):
    if where_clause is None:
        return table_data
    else:
        result = []
        for key, value in where_clause.items():
            for data in table_data:
                if data[key] == value:
                    result.append(data)
        return result

def update(table_data, set_clause, where_clause):
    for key, value in where_clause.items():
        for data in table_data:
            if data[key] == value:
                for item, val in set_clause.items():
                    data[item] = val
    return table_data

def delete(table_data, where_clause):
    result = []
    for key, value in where_clause.items():
        for data in table_data:
            if data[key] != value:
                result.append(data)
    return result