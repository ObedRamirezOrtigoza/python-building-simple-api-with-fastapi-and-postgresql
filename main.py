# main.py

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings  
import json


app = FastAPI()

class Stock(BaseModel):
    symbol: str
    stockname: str
    lastsale: str
    country: str
    ipoyear: Optional[int] = None

    
with open('stocks.json', 'r') as f:
    stocks = json.load(f)['stocks']



engine = create_engine(settings.sqlalchemy_database_url)  # Use sqlalchemy_database_url here
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



@app.get('/stock/{stock_symbol}', status_code=200)
def get_stock(stock_symbol: str) -> Stock:
    stock = [stock for stock in stocks if stock['symbol'] == stock_symbol]
    if len(stock) == 0:
        raise HTTPException(
            status_code=404, detail=f"No stock {stock_symbol} found."
         )

    return stock[0]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
