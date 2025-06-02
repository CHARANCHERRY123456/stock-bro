import os
import pandas as pd
from datetime import datetime

def analyze_trades_by_date(date_str: str):
    """
    Analyzes trade data for a given date and stores result in data/analysis.
    Format: YYYY-MM-DD
    """

    # Construct file path
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    input_path = f"data/uploads/{date_obj.year}/{date_obj.month:02d}/{date_obj.day:02d}/trades.csv"
    output_path = f"data/analysis/{date_str}-analysis.csv"

    if not os.path.exists(input_path):
        return {"error": f"No data found for {date_str}"}

    df = pd.read_csv(input_path)

    # Sanity checks
    if "ticker" not in df or "price" not in df or "quantity" not in df:
        return {"error": "Missing required columns in CSV."}

    # Calculate results
    result = df.groupby("ticker").agg(
        total_volume=("quantity", "sum"),
        avg_price=("price", "mean")
    ).reset_index()

    result.to_csv(output_path, index=False)

    return {
        "message": f"Analysis for {date_str} completed.",
        "output_file": output_path
    }
