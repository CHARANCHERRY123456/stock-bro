from pydantic import BaseModel, Field, validator
from datetime import datetime
import re

class TradeBase(BaseModel):
    ticker: str = Field(..., example="AAPL")
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)
    side: str = Field(..., pattern="^(buy|sell)$")
    timestamp: datetime

    @validator("ticker")
    def validate_ticker(cls, v):
        if not re.match(r"^[A-Z]{1,8}$", v):
            raise ValueError("Ticker must be 1-8 uppercase letters (A-Z)")
        return v

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id: int

    class Config:
        orm_mode = True
