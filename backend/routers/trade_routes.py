# backend/routers/trade_routes.py

from fastapi import APIRouter, HTTPException, Depends , Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from backend.schemas import trade_schema
from backend.crud import trade_crud

from backend.database import get_db


router = APIRouter(prefix="/trades", tags=["Trades"])

@router.post("/", response_model=trade_schema.Trade)
def add_trade(
    trade: trade_schema.TradeCreate,
    db: Session = Depends(get_db)
):
    """
    Add a new trade.
    """
    return trade_crud.create_trade(db=db, trade=trade)

@router.get("/", response_model=List[trade_schema.Trade])
def fetch_trades(
    ticker : Optional[str] = None,
    start_date : Optional[datetime] = Query(None),
    end_date : Optional[datetime] = Query(None),
    db : Session = Depends(get_db)
):
    """
    get  trades.
    """
    return trade_crud.get_trades(db=db , ticker=ticker , start_date=start_date,end_date=end_date)

