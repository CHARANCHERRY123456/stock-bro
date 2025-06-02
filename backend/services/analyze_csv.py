import pandas as pd
import os

def analyze_trades(file_path: str, output_dir: str):
    df = pd.read_csv(file_path)

    if 'ticker' not in df or 'price' not in df or 'quantity' not in df:
        raise ValueError("Missing required columns in CSV.")

    grouped = df.groupby("ticker").agg(
        total_volume=pd.NamedAgg(column="quantity", aggfunc="sum"),
        average_price=pd.NamedAgg(column="price", aggfunc="mean")
    ).reset_index()

    output_file = os.path.join(output_dir, "analysis.csv")
    grouped.to_csv(output_file, index=False)
    return output_file
