# backend/main.py

from fastapi import FastAPI
from backend.database import engine
from backend.models import trade_model
from backend.routers import trade_routes
from backend.routers import analysis_routes
from backend.routers import upload_router
from fastapi.middleware.cors import CORSMiddleware
print("Creating database tables...")
from sqlalchemy.exc import OperationalError
import logging

app = FastAPI(title="Stock-Bro API")

# Create tables on startup using FastAPI event
@app.on_event("startup")
def on_startup():
    try:
        trade_model.Base.metadata.create_all(bind=engine, checkfirst=True)
        print("Database tables created successfully.")
    except OperationalError:
        print("ERROR: Could not connect to the database. Please check your connection settings.")
        # Optionally, exit or re-raise if you want to stop the app
        # import sys; sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Allow CORS (frontend usage)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # i am allowing all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(trade_routes.router)
app.include_router(analysis_routes.router)