import pandas as pd
import numpy as np
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator


def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["Date"])
    df.sort_values("Date", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def apply_strategy(df: pd.DataFrame) -> pd.DataFrame:
    df["EMA20"] = EMAIndicator(close=df["Close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(close=df["Close"], window=50).ema_indicator()
    df["RSI"] = RSIIndicator(close=df["Close"], window=14).rsi()

    df["Signal"] = ""
    position = None  # None, "buy", or "sell"

    for i in range(1, len(df)):
        if (
            df["EMA20"].iloc[i] > df["EMA50"].iloc[i]
            and df["EMA20"].iloc[i - 1] <= df["EMA50"].iloc[i - 1]
            and df["RSI"].iloc[i] < 30
        ):
            df.at[i, "Signal"] = "BUY"
            position = "buy"
        elif (
            df["EMA20"].iloc[i] < df["EMA50"].iloc[i]
            and df["EMA20"].iloc[i - 1] >= df["EMA50"].iloc[i - 1]
            and df["RSI"].iloc[i] > 70
        ):
            df.at[i, "Signal"] = "SELL"
            position = "sell"
        else:
            df.at[i, "Signal"] = ""

    return df


def simulate(csv_path: str) -> pd.DataFrame:
    df = load_data(csv_path)
    df = apply_strategy(df)
    return df[["Date", "Close", "EMA20", "EMA50", "RSI", "Signal"]]

# print(simulate("data.csv").tail(10))