import asyncio
import websockets
import json
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.average import StockAverage
from backend.background_tasks import notify_price_threshold

price_history = {}

async def store_5min_averages():
    while True:
        await asyncio.sleep(300)  # 5 minutes
        db: Session = SessionLocal()
        try:
            for ticker, records in price_history.items():
                if not records:
                    continue

                avg_price = sum(p for (_, p) in records) / len(records)
                avg_entry = StockAverage(
                    ticker=ticker,
                    average_price=round(avg_price, 2),
                    calculated_at=datetime.utcnow()
                )
                db.add(avg_entry)

            db.commit()
            print("[INFO] 5-min average prices saved to DB.")

        finally:
            db.close()

async def process_updates():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            updates = json.loads(data)

            for stock in updates:
                ticker = stock["ticker"]
                price = stock["price"]
                timestamp = datetime.fromisoformat(stock["timestamp"])

                if ticker not in price_history:
                    price_history[ticker] = []

                price_history[ticker].append((timestamp, price))

                # Keep only data from last 1 minute for alert
                price_history[ticker] = [
                    (t, p) for (t, p) in price_history[ticker]
                    if t >= datetime.utcnow() - timedelta(minutes=1)
                ]

                if len(price_history[ticker]) > 1:
                    old_price = price_history[ticker][0][1]
                    percent_change = ((price - old_price) / old_price) * 100
                    if percent_change > 2:
                        print(f"[ALERT] {ticker} increased by {percent_change:.2f}% in last 1 min!")
                        # notify_price_threshold.delay(ticker, price, 2.0)  # Uncomment if Celery is running

async def main():
    await asyncio.gather(
        process_updates(),
        store_5min_averages()
    )

if __name__ == "__main__":
    asyncio.run(main())
