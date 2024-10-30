from sqlalchemy.orm import Session
import models

def init_db(db: Session):
    stocks = [
        models.Stock(
            symbol="TSLA",
            stockname="Tesla Inc. Common Stock",
            lastsale="$235.45",
            country="United States",
            ipoyear=2010,
            volume=1000000
        ),
        models.Stock(
            symbol="NVDA",
            stockname="NVIDIA Corporation Common Stock",
            lastsale="$477.76",
            country="United States",
            ipoyear=1999,
            volume=2000000
        ),
        models.Stock(
            symbol="AMZN",
            stockname="Amazon.com Inc. Common Stock",
            lastsale="$146.74",
            country="United States",
            ipoyear=1997,
            volume=1500000
        ),
    ]
    
    db.add_all(stocks)
    db.commit()
