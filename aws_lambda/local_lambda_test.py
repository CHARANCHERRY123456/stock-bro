import pandas as pd
import os

def local_lambda_test(date_str):
    input_path = f"data/uploads/{date_str}/stock.csv"
    output_path = f"data/analysis/{date_str}-analysis.csv"

    if not os.path.exists(input_path):
        print(f"No data found for {date_str}")
        return

    df = pd.read_csv(input_path)
    if 'ticker' not in df or 'price' not in df or 'quantity' not in df:
        print("Missing required columns in CSV.")
        return

    grouped = df.groupby('ticker').agg(
        total_volume=pd.NamedAgg(column='quantity', aggfunc='sum'),
        average_price=pd.NamedAgg(column='price', aggfunc='mean')
    ).reset_index()
    grouped.to_csv(output_path, index=False)
    print(f"Analysis complete. Output file: {output_path}")

if __name__ == "__main__":
    # Example: test for 2025-06-03
    local_lambda_test("2025-06-03")
