import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz  # Import pytz library for timezone support

symbols = ['ASHOKLEY.NS', 'BAJFINANCE.NS', 'DMART.NS', 'ENGINERSIN.NS', 'IBULHSGFIN.NS', 'INDUSINDBK.NS',
           'INFY.NS', 'LT.NS', 'MARUTI.NS', 'NATIONALUM.NS', 'SAIL.NS', 'SJVN.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS']

# Define the financial year
financial_year_start = datetime(2022, 4, 1)
financial_year_end = datetime(2023, 3, 31)

# Localize start and end dates to Asia/Kolkata timezone
start_date = pytz.timezone('Asia/Kolkata').localize(financial_year_start)
end_date = pytz.timezone('Asia/Kolkata').localize(financial_year_end)

dividends_list = []
splits_list = []

for symbol in symbols:
    stock = yf.Ticker(symbol)

    # Fetch and filter dividends for the financial year
    dividends = stock.dividends.reset_index()
    dividends = dividends[(dividends['Date'] >= start_date) & (dividends['Date'] <= end_date)]
    dividends.columns = [f"Date_{symbol}", f"Dividend_{symbol}"]
    dividends_list.append(dividends)

    # Fetch and filter splits for the financial year
    splits = stock.splits.reset_index()
    splits = splits[(splits['Date'] >= start_date) & (splits['Date'] <= end_date)]
    splits.columns = [f"Date_{symbol}", f"Split_{symbol}"]
    splits_list.append(splits)

# Merge all dividends data into a single DataFrame
dividends_data = dividends_list[0]
for dividends in dividends_list[1:]:
    dividends_data = dividends_data.merge(dividends, how='outer', left_index=True, right_index=True)

# Merge all splits data into a single DataFrame
splits_data = splits_list[0]
for splits in splits_list[1:]:
    splits_data = splits_data.merge(splits, how='outer', left_index=True, right_index=True)

print("Dividends DataFrame:")
print(dividends_data)

print("\nSplits DataFrame:")
print(splits_data)
