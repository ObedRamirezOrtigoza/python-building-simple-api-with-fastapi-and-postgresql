# settings.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    sqlalchemy_database_url: str  # Match the environment variable name

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
