from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_exppire_minutes: int = 60

    model_config= SettingsConfigDict(env_file= ".env")

@lru_cache
def get_settings()-> Settings:
    return Settings()






