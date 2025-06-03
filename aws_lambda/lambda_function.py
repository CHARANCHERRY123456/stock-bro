import boto3
import pandas as pd
import os
from io import StringIO

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event.get('bucket')
    date_str = event.get('date')  # format: YYYY/MM/DD
    if not bucket or not date_str:
        return {'error': 'Missing bucket or date parameter'}

    prefix = f"{date_str}/trades.csv"
    try:
        obj = s3.get_object(Bucket=bucket, Key=prefix)
        df = pd.read_csv(obj['Body'])
        if 'ticker' not in df or 'price' not in df or 'quantity' not in df:
            return {'error': 'Missing required columns in CSV.'}
        grouped = df.groupby('ticker').agg(
            total_volume=pd.NamedAgg(column='quantity', aggfunc='sum'),
            average_price=pd.NamedAgg(column='price', aggfunc='mean')
        ).reset_index()
        output_csv = grouped.to_csv(index=False)
        output_key = f"{date_str}/analysis_{date_str.replace('/', '-')}.csv"
        s3.put_object(Bucket=bucket, Key=output_key, Body=output_csv)
        return {'message': 'Analysis complete', 'output_file': output_key}
    except Exception as e:
        return {'error': str(e)}
