# backend/main.py

from fastapi import FastAPI
from backend.database import engine
from backend.models import trade_model
from backend.routers import trade_routes
from backend.routers import analysis_routes
from backend.routers import upload_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Stock-Bro API")

# Create tables on startup using FastAPI event
@app.on_event("startup")
def on_startup():
    trade_model.Base.metadata.create_all(bind=engine)


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