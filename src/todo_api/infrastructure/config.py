"""Typed environment configuration."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Python Drill To-Do API"
    mongodb_uri: str = "mongodb://127.0.0.1:27017"
    mongodb_database: str = "python_drill"


@lru_cache
def get_settings() -> Settings:
    return Settings()
