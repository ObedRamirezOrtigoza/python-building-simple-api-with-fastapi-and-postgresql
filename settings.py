
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str =  "postgresql://oro:password@localhost:5432/nasdaq_stocks"

    #sqlalchemy_string: str = "postgresql://user:passwordp@host/db"
    
settings = Settings()
