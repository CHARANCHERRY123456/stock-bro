import asyncio
import websockets
import json
import random
from datetime import datetime

stocks = {
    "AAPL": 180.0,
    "GOOGL": 2750.0,
    "MSFT": 310.0,
    "TSLA": 700.0
}

async def send_prices(websocket):
    while True:
        updates = []
        for ticker in stocks:
            change = random.uniform(-2, 2)
            stocks[ticker] += change
            updates.append({
                "ticker": ticker,
                "price": round(stocks[ticker], 2),
                "timestamp": datetime.utcnow().isoformat()
            })
        await websocket.send(json.dumps(updates))
        await asyncio.sleep(5)

async def main():
    async with websockets.serve(send_prices, "localhost", 8765):
        print("Mock WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
