from typing import Protocol

import json
import config
import redis


SETTINGS = config.get_settings()
MODE = SETTINGS.db_mode

class DBContext:
    def __init__(self, mode, settings):
        self.mode = mode
        if self.mode == "file":
            self.strategy = DBFileStrategy(settings)
        elif self.mode == "redis":
            self.strategy = DBRedisStrategy(settings)
        elif self.mode == "memory":
            self.strategy = DBMemoryStrategy(settings)

    def create(self, id: str, url: str) -> str:
        return self.strategy.create(id, url)

    def find(self, id: str) -> str | None:
        return self.strategy.find(id)

class DBStrategy(Protocol):
    def __init__(self, settings):
        ...
    def create(self, id: str, url: str) -> str:
        ...
    def find(self, id: str) -> str | None:
        ...

class DBFileStrategy(DBStrategy):
    def __init__(self, settings):
        self.settings = settings
        self.path = settings.db_file_path

    def read_database(self) -> dict:
        with open(self.path) as file:
            return json.load(file)

    def write_database(self, data: dict) -> dict:
        with open(self.path, 'w') as file:
            json.dump(data, file)
        return data

    def create(self, id: str, url: str) -> str:
        database = self.read_database()
        database[id] = url
        self.write_database(database)
        return id

    def find(self, id: str) -> str | None:
        database = self.read_database()
        return database.get(id)


class DBRedisStrategy:
    def __init__(self, settings):
        self.settings = settings
        self.conn = redis.Redis(
            self.settings.redis_host,
            self.settings.redis_port,
            decode_responses=True
        )

    def create(self, id: str, url: str) -> str:
        self.conn.set(id, url)
        return id

    def find(self, id: str) -> str | None:
        return self.conn.get(id)


class DBMemoryStrategy:
    def __init__(self, settings):
        self.settings = settings
        self.db = {}

    def create(self, id: str, url: str) -> str:
        self.db[id] = url
        return id

    def find(self, id: str) -> str | None:
        return self.db.get(id)


context = DBContext(MODE, SETTINGS)