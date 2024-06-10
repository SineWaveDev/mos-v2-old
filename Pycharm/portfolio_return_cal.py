import pandas as pd
import yfinance as yf


# File paths
file_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\Book1.xlsx'
df = pd.read_excel(file_path)

# Convert date columns to datetime objects
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], format='%d/%m/%Y')
df['Sale / Valuation Date'] = pd.to_datetime(df['Sale / Valuation Date'], format='%d/%m/%Y')



# Function to get daily prices for a given script
def get_daily_prices(script, start_date, end_date):
    data = yf.download(script, start=start_date, end=end_date)
    return data['Close']


# Create a new DataFrame to store transformed data
transformed_data = pd.DataFrame(columns=['Date', 'Name of Script', 'Quantity', 'Close Rate', 'Value'])

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    script_name = row['Name of Script']
    purchase_date = row['Purchase Date']
    sale_date = row['Sale / Valuation Date']
    qty = row['QTY']

    # Get daily prices for the script from purchase date to sale date
    daily_prices = get_daily_prices(script_name, purchase_date, sale_date)

    # Iterate over each day
    for date, price in daily_prices.iteritems():
        value = qty * price
        transformed_data = transformed_data.append({'Date': date,
                                                    'Name of Script': script_name,
                                                    'Quantity': qty,
                                                    'Close Rate': price,
                                                    'Value': value}, ignore_index=True)

# Save transformed data to Excel
transformed_data.to_excel("output_file.xlsx", index=False)







# import pandas as pd
# import yfinance as yf
#
# # File paths
# file_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\Book1.xlsx'
# output_excel_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm\stock_data_filled.xlsx'
#
# # Read the original Excel file into a pandas DataFrame
# df = pd.read_excel(file_path)
#
# stock_dfs = []
#
# for index, row in df.iterrows():
#     script_name = row['Name of Script']
#     start_date = pd.to_datetime(row['Purchase Date'], format='%d/%m/%Y')
#     end_date = pd.to_datetime(row['Sale / Valuation Date'], format='%d/%m/%Y')
#
#     stock_data = yf.download(script_name, start=start_date, end=end_date)
#     stock_data['Name of Script'] = script_name
#     stock_data['Purchase Date'] = start_date
#     stock_data['Sale / Valuation Date'] = end_date
#
#     stock_dfs.append(stock_data)
#
# # Concatenate all stock DataFrames into a single DataFrame
# combined_stock_df = pd.concat(stock_dfs)
#
# # Reset index if needed
# combined_stock_df.reset_index(inplace=True)
#
# # Save the combined DataFrame to an Excel file
# combined_stock_df.to_excel(output_excel_path, index=False)
#
# # Process merged data
# master_df = pd.DataFrame(columns=['source', 'dates', 'Name of Script', 'QTY', 'Value', 'Market_Rate'])
#
# # Iterate over rows of the original DataFrame
# for _, row in df.iterrows():
#     # Buy entry
#     buy_entry = {
#         'source': 'buy',
#         'dates': pd.to_datetime(row['Purchase Date'], format='%d/%m/%Y'),
#         'Name of Script': row['Name of Script'],
#         'QTY': row['QTY'],
#         'Value': row['Net Purchase Value'],
#         'Market_Rate': row['Rate']
#     }
#     # Sell entry
#     sell_entry = {
#         'source': 'sell',
#         'dates': pd.to_datetime(row['Sale / Valuation Date'], format='%d/%m/%Y'),
#         'Name of Script': row['Name of Script'],
#         'QTY': row['QTY'],
#         'Value': row['Net Sale / Market Value'],
#         'Market_Rate': row['Sale / Market Rate']
#     }
#     # Append entries to master_df
#     master_df = master_df._append(buy_entry, ignore_index=True)
#     master_df = master_df._append(sell_entry, ignore_index=True)
#
# # Sort master_df by dates
# master_df.sort_values(by='dates', inplace=True)
#
# # Process stock data
# stock_data = {}
# for _, row in master_df.iterrows():
#     date = row['dates']
#     script_name = row['Name of Script']
#     qty = row['QTY']
#     value = row['Value']
#     source = row['source']
#     Rate = row['Market_Rate']
#
#     if date not in stock_data:
#         stock_data[date] = {'Date': date}
#
#     if f'{script_name}_QTY' not in stock_data[date]:
#         stock_data[date][f'{script_name}_QTY'] = 0
#         stock_data[date][f'{script_name}_Value'] = 0
#         stock_data[date][f'{script_name}_Rate'] = 0
#
#     # Forward fill the data to get the last available values
#     for prev_date in sorted(stock_data.keys()):
#         if prev_date < date:
#             for stock in stock_data[prev_date]:
#                 if stock.endswith('_QTY') or stock.endswith('_Value') or stock.endswith('_Rate'):
#                     stock_data[date][stock] = stock_data[prev_date][stock]
#
#     if source == 'buy':
#         # Accumulate quantity and value for buy transactions
#         stock_data[date][f'{script_name}_QTY'] += qty
#         stock_data[date][f'{script_name}_Value'] += value
#         stock_data[date][f'{script_name}_Rate'] += Rate
#     elif source == 'sell':
#         # Subtract quantity and value for sell transactions
#         stock_data[date][f'{script_name}_QTY'] -= qty
#         stock_data[date][f'{script_name}_Value'] -= value
#         stock_data[date][f'{script_name}_Rate'] -= Rate
#
# # Create stock_df DataFrame
# stock_df = pd.DataFrame.from_dict(stock_data, orient='index').reset_index(drop=True)
# stock_df = stock_df[['Date'] + sorted([col for col in stock_df.columns if col != 'Date'])]
# stock_df_filled = stock_df.fillna(method='ffill')
#
#
# # Group the data by script name
# grouped_data = combined_stock_df.groupby('Name of Script')
#
# # Initialize an empty dataframe to store results
# stock_df_filled = pd.DataFrame(columns=['Script', 'Standard Deviation', 'Return'])
#
# # Calculate standard deviation and return for each group
# for script, data in grouped_data:
#     # Calculate daily returns
#     data['Return'] = data['Close'].pct_change()
#
#     # Calculate standard deviation
#     std_deviation = data['Return'].std()
#
#     # Calculate the mean return
#     mean_return = data['Return'].mean()
#
#     # Append the results to the new dataframe
#     stock_df_filled = stock_df_filled._append({'Script': script,
#                                               'Standard Deviation': std_deviation,
#                                               'Return': mean_return},
#                                              ignore_index=True)
#
# # Save the results to a new dataframe
# stock_df_filled.to_csv('stock_df_filled.csv', index=False)
#
# # Print the first few rows of the new dataframe
# print(stock_df_filled.head())
#
#
#
# # Define the path where you want to save the Excel file
# output_excel_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm\stock_data_filled.xlsx'
#
# # Save the DataFrame to an Excel file
# stock_df_filled.to_excel(output_excel_path, index=False)
#
# print("Stock data filled successfully saved to Excel file:", output_excel_path)
#
#
#
#
