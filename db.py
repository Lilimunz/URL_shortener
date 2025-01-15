DATABASE = {}


def create(id: str, url: str) -> str:
    DATABASE[id] = url
    return id

def find(id: str) -> str:
    return DATABASE[id]