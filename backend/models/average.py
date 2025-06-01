from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.database import Base
from datetime import datetime

class StockAverage(Base):
    __tablename__ = "stock_averages"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    average_price = Column(Float)
    calculated_at = Column(DateTime, default=datetime.utcnow)
