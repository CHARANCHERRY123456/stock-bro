# backend/main.py

from fastapi import FastAPI
from backend.database import engine
from backend.models import trade_model
from backend.routers import trade_routes
from fastapi.middleware.cors import CORSMiddleware

# Create tables on startup
trade_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock-Bro API")

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
