from fastapi import APIRouter, Query
from backend.services.analyze import analyze_trades_by_date

router = APIRouter()

@router.get("/analyze")
def analyze_trades(date: str = Query(..., example="2025-06-01")):
    """
    Analyze trades for a specific date (format: YYYY-MM-DD).
    """
    return analyze_trades_by_date(date)
