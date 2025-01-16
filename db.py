import json
import config
import redis

SETTINGS = config.get_settings()
MODE = SETTINGS.db_mode
PATH = 'database.json'
REDIS_CONN = redis.Redis(SETTINGS.redis_host, SETTINGS.redis_port, decode_responses=True)

def read_database() -> dict:
    with open(PATH) as file:
        return json.load(file)

def write_database(data: dict) -> dict:
    with open(PATH, 'w') as file:
        json.dump(data, file)
        return data

def create_on_file(id: str, url: str) -> str:
    database = read_database()
    database[id] = url
    write_database(database)
    return id

def find_on_file(id: str) -> str | None:
    database = read_database()
    return database.get(id)

def create_on_redis(id: str, url: str) -> str:
    REDIS_CONN.set(id, url)
    return id

def find_on_redis(id: str) -> str | None:
    return REDIS_CONN.get(id)

def create(id: str, url: str) -> str:
    if MODE == "file":
        return create_on_file(id, url)
    elif MODE == "redis":
        return create_on_redis(id, url)

def find(id: str) -> str | None:
    if MODE == "file":
        return find_on_file(id)
    elif MODE == "redis":
        return find_on_redis(id)
