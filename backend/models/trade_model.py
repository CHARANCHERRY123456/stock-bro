from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.database import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    side = Column(String)
    timestamp = Column(DateTime)
