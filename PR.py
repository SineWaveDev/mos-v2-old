
import yfinance as yf
import pandas as pd

# Define the ticker symbols and their weights
data = {
    'Ticker': ['ASHOKLEY.NS', 'BAJFINANCE.NS', 'DMART.NS', 'ENGINERSIN.NS', 'IBULHSGFIN.NS',
               'INDUSINDBK.NS', 'INFY.NS', 'LT.NS', 'MARUTI.NS', 'NATIONALUM.NS', 'SAIL.NS',
               'SJVN.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS'],
    'Weight': [0, 0.10239, 0.11166, 0, 0, 0, 0.09461, 0.16218, 0.22307, 0, 0, 0.07365, 0.23243, 0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the starting capital
capital = 1000000


# Function to fetch historical prices for a given ticker and date
def get_historical_price(ticker, start_date):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=pd.to_datetime('today').strftime('%Y-%m-%d'))
    return hist['Close'].iloc[0]  # Get the closing price of the first day


# Function to get the current price of a ticker
def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period='1d')['Close'].iloc[-1]
    return current_price


# Calculate the amount to invest in each stock
df['Investment'] = df['Weight'] * capital

# Fetch historical prices for each ticker on the start date
start_date = '2023-01-01'
df['Start_Price'] = df['Ticker'].apply(lambda x: get_historical_price(x, start_date))

# Calculate the quantity of each stock to purchase
df['Quantity'] = (df['Investment'] / df['Start_Price']).fillna(0)

# Fetch current prices for each ticker
df['Current_Price'] = df['Ticker'].apply(get_current_price)

# Calculate the current value of each investment
df['Current_Value'] = df['Quantity'] * df['Current_Price']

# Calculate the return on investment
df['Return'] = df['Current_Value'] - df['Investment']


# Function to transform each row
def transform_row(row):
    script_name = row['Ticker']
    asset_name = 'Richa Anil Moolani'  # You can adjust this according to your requirement
    purchase_date = '2023-01-01'  # Adjust this as per your data
    qty = row['Quantity']
    rate = row['Start_Price']
    net_purchase_value = row['Investment']
    sale_valuation_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Adjust this as per your requirement
    sale_market_rate = row['Current_Price']
    net_sale_market_value = row['Current_Value']
    realized_profit_loss = row['Return']
    unrealized_profit_loss = 0  # You need to calculate this based on current market conditions
    total_profit_loss = realized_profit_loss + unrealized_profit_loss
    days = (pd.to_datetime('today') - pd.to_datetime(purchase_date)).days
    # ann_return_percent = (total_profit_loss / net_purchase_value) * (365 / days) * 100
    weightage = row['Weight']


    return pd.Series([script_name, asset_name, purchase_date, qty, rate, net_purchase_value,
                      sale_valuation_date, sale_market_rate, net_sale_market_value,
                      realized_profit_loss, unrealized_profit_loss, total_profit_loss,
                      days, weightage],
                     index=['Name of Script', 'Ass Name', 'Purchase Date', 'QTY', 'Rate',
                            'Net Purchase Value', 'Sale / Valuation Date', 'Sale / Market Rate',
                            'Net Sale / Market Value', 'Realized (Profit/ Loss)', 'Unrealized (Profit/ Loss)',
                            'Total (Profit/ Loss)', 'Days', 'Weightage'])


# Apply the function to each row of the DataFrame
transformed_df = df.apply(transform_row, axis=1)

# Print the transformed DataFrame
print(transformed_df)

# Save DataFrame to an Excel file in the download folder
file_path = r"C:\Users\Sinewave#2022\Downloads/stock_portfolio_transformed.xlsx"  # Replace 'path_to_your_download_folder' with your actual path
transformed_df.to_excel(file_path, index=False)
print("Transformed DataFrame saved to:", file_path)
