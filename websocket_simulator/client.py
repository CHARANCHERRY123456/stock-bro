import asyncio
import websockets
import json
from datetime import datetime, timedelta

print("in the client")
price_history = {}

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

                # Keep only last 1 minute data
                price_history[ticker] = [
                    (t, p) for (t, p) in price_history[ticker]
                    if t >= datetime.utcnow() - timedelta(minutes=1)
                ]

                old_price = price_history[ticker][0][1]
                percent_change = ((price - old_price) / old_price) * 100

                if percent_change > 2:
                    print(f"[ALERT] {ticker} increased by {percent_change:.2f}% in last 1 min!")

if __name__ == "__main__":
    asyncio.run(process_updates())
