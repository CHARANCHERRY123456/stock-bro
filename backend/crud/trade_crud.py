from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from backend import models
from backend.schemas import trade_schema

def create_trade(db: Session, trade: trade_schema.TradeCreate) -> models.trade_model.Trade:
    db_trade = models.trade_model.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(
    db: Session,
    ticker: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> List[models.trade_model.Trade]:
    query = db.query(models.trade_model.Trade)

    if ticker:
        query = query.filter(models.trade_model.Trade.ticker == ticker)
    if start_date:
        query = query.filter(models.trade_model.Trade.timestamp >= start_date)
    if end_date:
        query = query.filter(models.trade_model.Trade.timestamp <= end_date)

    return query.all()
