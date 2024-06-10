import pandas as pd
import yfinance as yf
from pandas.tseries.offsets import BDay

# Define the capital and dates
capital = 1000000
start_date = '2023-05-29'
end_date = '2024-05-29'

# Adjust start and end dates to the nearest business day if they fall on a non-trading day
start_date = pd.to_datetime(start_date) - BDay(0)
end_date = pd.to_datetime(end_date) - BDay(0)

# Provided data
data = {
    'Ticker': ['ASHOKLEY.NS', 'BAJFINANCE.NS', 'DMART.NS', 'ENGINERSIN.NS', 'IBULHSGFIN.NS', 'INDUSINDBK.NS', 'INFY.NS',
               'LT.NS', 'MARUTI.NS', 'NATIONALUM.NS', 'SAIL.NS', 'SJVN.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS'],
    'Weight': [0.08609, 0.02222, 0.13907, 0, 0, 0, 0.11977, 0.20433, 0.17414, 0, 0, 0.10154, 0.15284, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Filter out stocks with zero weight
df = df[df['Weight'] > 0]

# Download historical data for the tickers
tickers = df['Ticker'].tolist()
data = yf.download(tickers, start=start_date.strftime('%Y-%m-%d'), end=(end_date + pd.Timedelta(days=1)).strftime('%Y-%m-%d'))

# Calculate the initial investment for each stock
df['Initial Investment'] = df['Weight'] * capital

# Get the adjusted close prices
adj_close = data['Adj Close']

# Get the prices on the nearest available trading days
start_prices = adj_close.loc[adj_close.index.asof(start_date)]
end_prices = adj_close.loc[adj_close.index.asof(end_date)]

# Calculate the number of shares purchased for each stock
df['Shares'] = df.apply(lambda row: row['Initial Investment'] / start_prices[row['Ticker']], axis=1)

# Calculate the final value of each investment
df['Final Value'] = df.apply(lambda row: row['Shares'] * end_prices[row['Ticker']], axis=1)

# Calculate the total portfolio return
total_initial_investment = df['Initial Investment'].sum()
total_final_value = df['Final Value'].sum()
portfolio_return = (total_final_value - total_initial_investment) / total_initial_investment

print(f'Total Portfolio Return: {portfolio_return * 100:.2f}%')

