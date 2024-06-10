# import numpy as np
# import pandas as pd
# import yfinance as yf
# import datetime as dt
# import copy
# import matplotlib.pyplot as plt
# import calendar
#
# def CAGR(DF):
#     "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
#     df = DF.copy()
#     df["cum_return"] = (1 + df["mon_ret"]).cumprod()
#     n = len(df)/12
#     CAGR = (df["cum_return"].tolist()[-1])**(1/n) - 1
#     return CAGR
#
# def volatility(DF):
#     "function to calculate annualized volatility of a trading strategy"
#     df = DF.copy()
#     vol = df["mon_ret"].std() * np.sqrt(12)
#     return vol
#
# def sharpe(DF,rf):
#     "function to calculate sharpe ratio ; rf is the risk free rate"
#     df = DF.copy()
#     sr = (CAGR(df) - rf)/volatility(df)
#     return sr
#
# def max_dd(DF):
#     "function to calculate max drawdown"
#     df = DF.copy()
#     df["cum_return"] = (1 + df["mon_ret"]).cumprod()
#     df["cum_roll_max"] = df["cum_return"].cummax()
#     df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
#     df["drawdown_pct"] = df["drawdown"]/df["cum_roll_max"]
#     max_dd = df["drawdown_pct"].max()
#     return max_dd
#
# # Download historical data (monthly) for DJI constituent stocks
#
# tickers = [
#     "BRITANNIA.NS",
#     "TITAN.NS",
#     "LT.NS",
#     "ONGC.NS",
#     "HEROMOTOCO.NS",
#     "ULTRACEMCO.NS",
#     "ADANIENT.NS",
#     "HINDALCO.NS",
#     "BAJFINANCE.NS",
#     "HDFCLIFE.NS",
#     "BAJAJFINSV.NS",
#     "RELIANCE.NS",
#     "APOLLOHOSP.NS",
#     "TCS.NS",
#     "TATASTEEL.NS",
#     "MARUTI.NS",
#     "KOTAKBANK.NS",
#     "NESTLEIND.NS",
#     "INDUSINDBK.NS",
#     "WIPRO.NS",
#     "ITC.NS",
#     "NTPC.NS",
#     "TATACONSUM.NS",
#     "LTIM.NS",
#     "BHARTIARTL.NS",
#     "CIPLA.NS"
# ]
#
# ohlc_mon = {} # directory with ohlc value for each stock
# start = dt.datetime.today()-dt.timedelta(1825)
# end = dt.datetime.today()
#
# # looping over tickers and creating a dataframe with close prices
# for ticker in tickers:
#     ohlc_mon[ticker] = yf.download(ticker,start,end,interval='1mo')
#     ohlc_mon[ticker].dropna(inplace=True,how="all")
#
# tickers = ohlc_mon.keys() # redefine tickers variable after removing any tickers with corrupted data
#
# # calculating monthly return for each stock and consolidating return info by stock in a separate dataframe
# return_df = pd.DataFrame()
# for ticker in tickers:
#     print("calculating monthly return for ",ticker)
#     ohlc_mon[ticker]["mon_ret"] = ohlc_mon[ticker]["Adj Close"].pct_change()
#     return_df[ticker] = ohlc_mon[ticker]["mon_ret"]
# return_df.dropna(inplace=True)
#
# # function to calculate portfolio return iteratively
# # function to calculate portfolio return iteratively
# # function to calculate portfolio return iteratively
# # function to calculate portfolio return iteratively
# def pflio(DF, m, x, save_file=None):
#     df = DF.copy()
#     portfolio = []
#     monthly_ret = [0]
#     portfolio_history = []  # To store portfolio selections
#
#     # List to store monthly returns for each stock
#     monthly_stock_returns = {ticker: [] for ticker in df.columns}
#
#     for i in range(len(df)):
#         if len(portfolio) > 0:
#             monthly_ret.append(df[portfolio].iloc[i, :].mean())
#             bad_stocks = df[portfolio].iloc[i, :].sort_values(ascending=True)[:x].index.values.tolist()
#             portfolio = [t for t in portfolio if t not in bad_stocks]
#         fill = m - len(portfolio)
#         new_picks = df.iloc[i, :].sort_values(ascending=False)[:fill].index.values.tolist()
#         portfolio = portfolio + new_picks
#         portfolio_history.append(portfolio)  # Save portfolio selection
#
#         # Record monthly returns for each stock
#         for ticker in df.columns:
#             monthly_stock_returns[ticker].append(df[ticker].iloc[i])
#
#     monthly_ret_df = pd.DataFrame(np.array(monthly_ret), columns=["mon_ret"])
#
#     # Convert portfolio history to DataFrame and save to CSV if save_file parameter is provided
#     if save_file:
#         # Create a list of lists to store portfolio history with returns appended to each stock
#         portfolio_with_returns = []
#
#         # Add the header row to portfolio_with_returns
#         header_row = ["Month", "Stock1", "Return1", "Stock2", "Return2", "Stock3", "Return3", "Stock4", "Return4",
#                       "Stock5", "Return5", "Stock6", "Return6"]
#         portfolio_with_returns.append(header_row)
#
#         # Iterate through the portfolio history and add data to portfolio_with_returns
#         for i, portfolio_selection in enumerate(portfolio_history):
#             # Calculate month and year
#             month_index = (i + 3) % 12
#             year = 19 + (i + 3) // 12
#             if month_index == 0:
#                 year -= 1  # Adjust the year if the month is December
#             month_abbr = calendar.month_abbr[month_index]
#
#             portfolio_row = [f"{month_abbr}-{str(year)}"]
#             for j, stock in enumerate(portfolio_selection):
#                 portfolio_row.append(stock)
#                 portfolio_row.append(monthly_stock_returns[stock][i])
#             portfolio_with_returns.append(portfolio_row)
#
#         # Save portfolio history to CSV
#         with open(save_file, 'w') as f:
#             for portfolio_row in portfolio_with_returns:
#                 f.write(','.join(map(str, portfolio_row)) + '\n')
#
#     return monthly_ret_df
#
#
#
#
# #calculating overall strategy's KPIs
# strategy_return = pflio(return_df, 6, 3, save_file='portfolio_history.csv')
# strategy_cagr = CAGR(strategy_return)
# strategy_sharpe = sharpe(strategy_return, 0.025)
# strategy_max_dd = max_dd(strategy_return)
#
# #calculating KPIs for Index buy and hold strategy over the same period
# # Download historical data and calculate KPIs for each stock
# stock_cagrs = {}
# stock_sharpes = {}
# stock_max_dds = {}
#
# for ticker in tickers:
#     stock_data = yf.download(ticker, dt.date.today() - dt.timedelta(1825), dt.date.today(), interval='1mo')
#     stock_data["mon_ret"] = stock_data["Adj Close"].pct_change().fillna(0)
#
#     # Calculate KPIs for the stock
#     stock_cagrs[ticker] = CAGR(stock_data)
#     stock_sharpes[ticker] = sharpe(stock_data, 0.025)
#     stock_max_dds[ticker] = max_dd(stock_data)
#
#
# #visualization
# # Save portfolio data to CSV
# return_df.to_csv('portfolio_data.csv')
#
# # Save visualization as a PNG file
# fig, ax = plt.subplots()
# plt.plot((1+strategy_return).cumprod())
# plt.plot((1+stock_data["mon_ret"].reset_index(drop=True)).cumprod())
# plt.title("Index Return vs Strategy Return")
# plt.ylabel("Cumulative Return")
# plt.xlabel("Months")
# ax.legend(["Strategy Return","Index Return"])
# plt.savefig('portfolio_comparison.png')
# plt.show()
import pandas as pd

# Read the portfolio data from an Excel file
portfolio_data = pd.read_excel(r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm\stock_data_filled..........xlsx')

# Calculate the total value for each stock across all dates
total_value_per_stock = portfolio_data.groupby(portfolio_data.columns.str.extract('([A-Z]+[.]NS)', expand=False), axis=1).sum()

# Calculate the total portfolio value for each date
total_portfolio_value = total_value_per_stock.sum(axis=1)

# Calculate the percentage each stock represents out of the total portfolio value
percentage_per_stock = (total_value_per_stock / total_portfolio_value) * 100

# Print the resulting DataFrame showing the percentage each stock represents
print(percentage_per_stock)
