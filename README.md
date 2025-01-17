- Encurtador de links

requirements
- core
    Dado uma url, gerar uma url imutável única e menor que redirecione para o mesmo endereço.
    Servir todas urls cadastradas no sistema

Environment Variables:

REDIS_HOST
REDIS_PORT
DB_MODE
DB_FILE_PATH

Install Dependencies

```
pip install redis fastapi pydantic_settings
```

Run API Project

```
fastapi dev api.py
```

Run CLI

```
python cli.py -h
```
