from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from backend.config import DATABASE_URL

DATABASE_URL = "postgresql://postgres:ChXRdHnBewpbIdErnPFXZBuKzruvRyBs@shortline.proxy.rlwy.net:50850/railway"
DATABASE_URL = "postgresql://postgres:XInLULFfOTiTxNafUbGxLwvCGUONEroc@maglev.proxy.rlwy.net:24997/railway"
engine = create_engine(DATABASE_URL)
print("Database engine created successfully.")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Do NOT import models here to avoid circular imports

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
