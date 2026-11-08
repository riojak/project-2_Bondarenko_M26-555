import json


def load_metadata(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return {}

def save_metadata(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file)
