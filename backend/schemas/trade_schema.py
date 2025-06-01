from pydantic import BaseModel, Field
from datetime import datetime

class TradeBase(BaseModel):
    ticker: str = Field(..., example="AAPL")
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)
    side: str = Field(..., pattern="^(buy|sell)$")
    timestamp: datetime

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id: int

    class Config:
        orm_mode = True
