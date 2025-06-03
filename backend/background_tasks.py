# Celery configuration for background tasks
from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "stockbro_tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)

@celery_app.task
def notify_price_threshold(ticker: str, price: float, threshold: float):
    # In a real app, send email/SMS/notification
    print(f"[NOTIFY] {ticker} crossed threshold: {price} > {threshold}")
    return True