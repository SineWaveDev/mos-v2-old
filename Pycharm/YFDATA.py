import yfinance as yf
import pandas as pd

# Define the ticker symbols
tickers = [    'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'AXISBANK.NS', 'HINDUNILVR.NS',
    'ICICIBANK.NS', 'WIPRO.NS', 'CIPLA.NS', 'TECHM.NS', 'ONGC.NS',
    'BPCL.NS', 'SBIN.NS', 'NTPC.NS', 'RELIANCE.NS', 'ADANIPORTS.NS',
    'TITAN.NS', 'HCLTECH.NS', 'BAJFINANCE.NS', 'UPL.NS', 'SBIN.NS']

# Download historical data for the tickers
data = yf.download(tickers, start="2019-01-01", end="2024-03-20", interval="1mo")['Close']

# Resample data on monthly basis and get the last day of each month
data_monthly = data.resample('M').last()

# Write the data to a single sheet in an Excel file
with pd.ExcelWriter('historical_data_Demo.xlsx') as writer:
    data_monthly.to_excel(writer, sheet_name='Close Prices')

print("dta save successfully")

