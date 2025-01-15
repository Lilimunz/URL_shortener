DATABASE = {}


def create(id: str, url: str) -> str:
    DATABASE[id] = url
    return id

def find(id: str) -> str | None:
    return DATABASE.get(id)