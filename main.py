# main.py

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings  # Import your settings module

app = FastAPI()

# Use the correct attribute name
engine = create_engine(settings.sqlalchemy_database_url)  # Use sqlalchemy_database_url here
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
