# 📚 Stock-Bro: The Friendly Stock Trading Adventure!

Welcome to **Stock-Bro** – a project that turns the world of stock trading and analysis into a fun, interactive story! Whether you’re a curious kid, a beginner, or a developer, this guide will help you explore, test, and understand every part of this magical stock journey.

---

## 🏁 The Story Begins: What is Stock-Bro?

Imagine you have a magical notebook where you can write down all your stock trades, ask questions about them, and even play with pretend money to see what would happen if you tried different trading tricks. Stock-Bro is that notebook, but on your computer!

It’s a project that lets you:
- **Upload your trades** (like writing in your notebook)
- **Analyze your trades** (get instant feedback and fun facts)
- **Simulate trading strategies** (play with pretend money and see what works)
- **Watch real-time stock prices** (like watching a stock race on TV)
- **(Optionally) Use the cloud** (for those who want to fly even higher!)

---

## 🧩 The Magic Pieces: What’s Inside?

- **FastAPI Backend**: The friendly librarian who listens to your requests and helps you manage your trades.
- **PostgreSQL Database**: The big book where all your trades are safely stored.
- **WebSocket Simulator**: The TV that shows you live stock price races!
- **Trading Simulator**: The playground where you try out different trading tricks.
- **AWS Lambda (Optional)**: The cloud wizard who can analyze your trades in the sky (but you don’t need him if you don’t have an AWS account).

---

## 🚦 How to Start Your Adventure

### 1. **Set Up Your Tools**
- Make sure you have Python 3.8+ installed.
- Install the magic spells (dependencies):
  ```bash
  pip install -r requirements.txt
  ```

### 2. **Start the Librarian (FastAPI Backend)**
- Run this command:
  ```bash
  uvicorn backend.main:app --reload
  ```
- Visit `http://localhost:8000/docs` in your browser to see all the things you can ask the librarian to do!

### 3. **Upload Your Trades**
- Use the `/api/upload-csv/` endpoint to upload a CSV file of your trades (like `data/uploads/2025-06-03/stock.csv`).
- The librarian will read your trades and write a report for you!

### 4. **Analyze Your Trades**
- Use the `/analyze?date=YYYY-MM-DD` endpoint to get a summary of your trades for a specific day.
- The report will be saved in `data/analysis/`.

### 5. **Watch the Stock Race (WebSocket Simulator)**
- Open two terminals:
  - In one, run:
    ```bash
    python3 websocket_simulator/mock_server.py
    ```
  - In the other, run:
    ```bash
    python3 websocket_simulator/client.py
    ```
- Watch as the TV shows you live price updates and alerts if a stock zooms up by more than 2% in a minute!

### 6. **Play with Trading Strategies**
- Try the trading playground:
  ```bash
  python3 backend/strategy/trading_simulator.py
  ```
- See the buy/sell signals and your pretend profit or loss in `simulation_report.txt`.

### 7. **(Optional) Call the Cloud Wizard (AWS Lambda)**
- If you have an AWS account, you can use `aws_lambda/lambda_function.py` to analyze trades in the cloud.
- If not, use the local test script:
  ```bash
  python3 aws_lambda/local_lambda_test.py
  ```
- The report will appear in `data/analysis/`.

---

## 🧙‍♂️ The Magic Explained (For Curious Kids & Beginners)
- **API**: Like a menu at a restaurant. You tell the librarian what you want, and they bring it to you.
- **Database**: Like a big diary where every trade is written down.
- **WebSocket**: Like a live TV channel for stocks.
- **Simulation**: Like playing a board game with pretend money.
- **Cloud (AWS)**: Like sending your homework to a wizard in the sky (but you can do everything on your own computer too!).

---

## 📝 How to Test Everything
- Try uploading a CSV and see the analysis file appear.
- Watch the WebSocket client for live alerts.
- Run the trading simulator and check your results.
- Use the local Lambda test script to analyze trades without AWS.

---

## 💡 Tips & Notes
- You don’t need AWS or any paid services to enjoy Stock-Bro.
- All your data stays on your computer unless you want to use the cloud.
- The code is written to be easy to read and change, so feel free to explore and play!

---

## 🎉 The End (Or a New Beginning!)

Congratulations! You’ve finished the Stock-Bro adventure. You can now upload, analyze, and play with stock trades like a pro. If you want to add more magic, you can always extend the project with new features.

Happy trading and learning! 🚀