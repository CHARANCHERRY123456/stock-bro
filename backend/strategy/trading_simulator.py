import pandas as pd

def load_data(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    return df

def calculate_moving_averages(df, short_window=50, long_window=200):
    df['SMA_50'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_200'] = df['Close'].rolling(window=long_window).mean()
    return df

def generate_signals(df):
    df['Signal'] = 0
    df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1  # Buy
    df.loc[df['SMA_50'] < df['SMA_200'], 'Signal'] = -1  # Sell
    return df

def simulate_trades(df, initial_capital=10000):
    df['Position'] = df['Signal'].diff()
    cash = initial_capital
    shares = 0
    trades = []

    for _, row in df.iterrows():
        if row['Position'] == 1:  # Buy
            shares = cash // row['Close']
            cash -= shares * row['Close']
            trades.append(f"Buy on {row['Date'].date()} at {row['Close']}")
        elif row['Position'] == -1 and shares > 0:  # Sell
            cash += shares * row['Close']
            trades.append(f"Sell on {row['Date'].date()} at {row['Close']}")
            shares = 0

    final_value = cash + shares * df.iloc[-1]['Close']
    profit = final_value - initial_capital
    return trades, profit

def run_simulation(csv_file):
    df = load_data(csv_file)
    df = calculate_moving_averages(df)
    df = generate_signals(df)
    trades, profit = simulate_trades(df)

    print("Trade Log:")
    for trade in trades:
        print(trade)
    print(f"\nTotal Profit/Loss: ₹{profit:.2f}")

# Example usage
if __name__ == "__main__":
    run_simulation("data/historical/AAPL.csv")
