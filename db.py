import json

PATH = 'database.json'

def read_database() -> dict:
    with open(PATH) as file:
        return json.load(file)

def write_database(data: dict) -> dict:
    with open(PATH, 'w') as file:
        json.dump(data, file)
        return data

def create(id: str, url: str) -> str:
    database = read_database()
    database[id] = url
    write_database(database)
    return id

def find(id: str) -> str | None:
    database = read_database()
    return database.get(id)