from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    redis_host: str
    redis_port: str
    db_mode: str
    db_file_path: str
    model_config = SettingsConfigDict(env_file=".env")

def get_settings():
    return Settings()
