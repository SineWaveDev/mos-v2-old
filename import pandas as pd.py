

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from pypfopt import EfficientFrontier, expected_returns, risk_models

# List of stock tickers
tickers = ['ASHOKLEY.NS', 'BAJFINANCE.NS', 'DMART.NS', 'ENGINERSIN.NS', 'IBULHSGFIN.NS', 'INDUSINDBK.NS',
           'INFY.NS', 'LT.NS', 'MARUTI.NS', 'NATIONALUM.NS', 'SAIL.NS', 'SJVN.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS']


end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

data_current = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

mu_current = expected_returns.mean_historical_return(data_current)
Sigma_current = risk_models.sample_cov(data_current)

Sigma_current = (Sigma_current + Sigma_current.T) / 2

risk_free_rate = 0.07

ef = EfficientFrontier(mu_current, Sigma_current)

ef.add_constraint(lambda w: w >= 0)

ef.efficient_return(target_return=0.8)

cleaned_weights = ef.clean_weights()

expected_return_current, volatility_current, sharpe_ratio_current = ef.portfolio_performance(risk_free_rate=risk_free_rate)

end_date_prev = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
start_date_prev = (datetime.today() - timedelta(days=365*2)).strftime('%Y-%m-%d')

data_prev = yf.download(tickers, start=start_date_prev, end=end_date_prev)['Adj Close']

initial_investment = 1000000  # Assuming an initial investment of 1,000,000 units

shares = {ticker: (initial_investment * weight) / data_prev.iloc[0][ticker] for ticker, weight in cleaned_weights.items()}

final_portfolio_value_prev = sum([shares[ticker] * data_prev.iloc[-1][ticker] for ticker in shares])

total_return_prev = (final_portfolio_value_prev - initial_investment) / initial_investment

portfolio_data = pd.DataFrame(columns=["Ticker", "Weight", "Expected Return", "Volatility", "Sharpe Ratio", "Risk Free Rate", "Total Return Previous Year"])

for ticker, weight in cleaned_weights.items():
    portfolio_data = portfolio_data._append({"Ticker": ticker, "Weight": weight}, ignore_index=True)

portfolio_data.loc[0, "Expected Return"] = expected_return_current
portfolio_data.loc[0, "Volatility"] = volatility_current
portfolio_data.loc[0, "Sharpe Ratio"] = sharpe_ratio_current
portfolio_data.loc[0, "Risk Free Rate"] = risk_free_rate
portfolio_data.loc[0, "Total Return Previous Year"] = total_return_prev

excel_filename = "portfolio_performance_comparison.xlsx"
portfolio_data.to_excel(excel_filename, index=False)

print("Portfolio performance data saved to:", excel_filename)

