from fastapi import APIRouter
# from app.api.routes import upload
from backend.routers import upload_router

router = APIRouter()
router.include_router(upload_router.router, prefix="/api")
