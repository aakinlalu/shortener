from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env_name: str = "local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    settings = Settings()
    print(f"Loading settings from {settings.env_name} environment")
    return settings
