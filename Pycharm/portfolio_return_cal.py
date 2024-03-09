import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

file_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\Book1.xlsx'


output_excel_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm/finance_data.xlsx'
output_merged_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm/merged_data.xlsx'

# Read the original Excel file into a pandas DataFrame
df = pd.read_excel(file_path)
#
# # Fetch stock data and store in dictionary
# stock_dfs = {}
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
#     if script_name not in stock_dfs:
#         stock_dfs[script_name] = stock_data
#     else:
#         stock_dfs[script_name] = pd.concat([stock_dfs[script_name], stock_data], ignore_index=False)
#
# # Save each stock's data into separate sheets in an Excel file
# with pd.ExcelWriter(output_excel_path) as writer:
#     for script_name, stock_df in stock_dfs.items():
#         stock_df.to_excel(writer, sheet_name=script_name, index=False)
# print("Finance data saved successfully.")

# Process merged data
master_df = pd.DataFrame(columns=['source', 'dates', 'Name of Script', 'QTY', 'Value', 'Market_Rate'])

# Iterate over rows of the original DataFrame
for _, row in df.iterrows():
    # Buy entry
    buy_entry = {
        'source': 'buy',
        'dates': pd.to_datetime(row['Purchase Date'], format='%d/%m/%Y'),
        'Name of Script': row['Name of Script'],
        'QTY': row['QTY'],
        'Value': row['Net Purchase Value'],
        'Market_Rate': row['Rate']
    }
    # Sell entry
    sell_entry = {
        'source': 'sell',
        'dates': pd.to_datetime(row['Sale / Valuation Date'], format='%d/%m/%Y'),
        'Name of Script': row['Name of Script'],
        'QTY': row['QTY'],
        'Value': row['Net Sale / Market Value'],
        'Market_Rate': row['Sale / Market Rate']
    }
    # Append entries to master_df
    master_df = master_df._append(buy_entry, ignore_index=True)
    master_df = master_df._append(sell_entry, ignore_index=True)

# Sort master_df by dates
master_df.sort_values(by='dates', inplace=True)
print(master_df)

# Process stock data
stock_data = {}
# Process stock data
stock_data = {}
for _, row in master_df.iterrows():
    date = row['dates']
    script_name = row['Name of Script']
    qty = row['QTY']
    value = row['Value']
    source = row['source']
    Rate = row['Market_Rate']

    if date not in stock_data:
        stock_data[date] = {'Date': date}

    if f'{script_name}_QTY' not in stock_data[date]:
        stock_data[date][f'{script_name}_QTY'] = 0
        stock_data[date][f'{script_name}_Value'] = 0
        stock_data[date][f'{script_name}_Rate'] = 0

    # Forward fill the data to get the last available values
    for prev_date in sorted(stock_data.keys()):
        if prev_date < date:
            for stock in stock_data[prev_date]:
                if stock.endswith('_QTY') or stock.endswith('_Value') or stock.endswith('_Rate'):
                    stock_data[date][stock] = stock_data[prev_date][stock]

    if source == 'buy':
        # Accumulate quantity and value for buy transactions
        stock_data[date][f'{script_name}_QTY'] += qty
        stock_data[date][f'{script_name}_Value'] += value
        stock_data[date][f'{script_name}_Rate'] += Rate

        # Create stock_df DataFrame
        stock_df = pd.DataFrame.from_dict(stock_data, orient='index').reset_index(drop=True)
        stock_df = stock_df[['Date'] + sorted([col for col in stock_df.columns if col != 'Date'])]
        stock_df_filled = stock_df.fillna(method='ffill')


    elif source == 'sell':
        # Subtract quantity and value for sell transactions
        stock_data[date][f'{script_name}_QTY'] -= qty
        stock_data[date][f'{script_name}_Value'] -= value
        stock_data[date][f'{script_name}_Rate'] -= Rate

        # Create stock_df DataFrame
        stock_df = pd.DataFrame.from_dict(stock_data, orient='index').reset_index(drop=True)
        stock_df = stock_df[['Date'] + sorted([col for col in stock_df.columns if col != 'Date'])]
        stock_df_filled = stock_df.fillna(method='ffill')

# Create stock_df DataFrame
stock_df = pd.DataFrame.from_dict(stock_data, orient='index').reset_index(drop=True)
stock_df = stock_df[['Date'] + sorted([col for col in stock_df.columns if col != 'Date'])]
stock_df_filled = stock_df.fillna(method='ffill')

print(stock_df_filled)





# Define the path where you want to save the Excel file
output_excel_path = r'C:\Users\Sinewave#2022\OneDrive - Sinewave\Desktop\SAGAR_TAXBACE_2_PROJECT\Pycharm\stock_data_filled.xlsx'

# Save the DataFrame to an Excel file
stock_df_filled.to_excel(output_excel_path, index=False)

print("Stock data filled successfully saved to Excel file:", output_excel_path)








# stock_df_filled.to_excel("merged_data_with_dates_and_ohlc.xlsx", index=False)
# print("Updated Excel file saved successfully.")

# # Merge stock data
# for script_name, stock_df in stock_dfs.items():
#     stock_df['Date'] = stock_df.index
#     stock_df.reset_index(drop=True, inplace=True)
#     stock_dfs[script_name] = stock_df
#
# open_dfs = []
# for script_name, stock_df in stock_dfs.items():
#     open_df = stock_df[['Open', 'Date']].copy()
#     open_df.rename(columns={'Open': f'{script_name}_Open'}, inplace=True)
#     open_dfs.append(open_df)
#
# open_data_df = pd.concat(open_dfs, axis=1)
# stock_df_filled.rename(columns={'Date': 'Date_filled'}, inplace=True)
# #
# # print("Columns of open_data_df:", open_data_df.columns)
# # print("Columns of stock_df_filled:", stock_df_filled.columns)
# #
# # import pandas as pd
#
# # Load your open_data_df and stock_df_filled DataFrames
# # Make sure they are properly loaded before proceeding
#
# # Find the date columns in open_data_df and stock_df_filled
# date_columns_open = [col for col in open_data_df.columns if 'Date' in col]
# date_columns_stock = [col for col in stock_df_filled.columns if 'Date' in col]
#
# # Concatenate all date columns and find the unique dates
# all_dates = pd.concat([open_data_df[date_columns_open], stock_df_filled[date_columns_stock]], axis=1).stack().unique()
#
# # Create a DataFrame with the complete date range
# complete_date_range_df = pd.DataFrame(all_dates, columns=['Date'])
#
# # Merge the stock prices with the complete date range
# merged_df = pd.merge(complete_date_range_df, stock_df_filled, how='left', left_on='Date', right_on=date_columns_stock[0])
#
# # Forward-fill missing values in the stock prices
# merged_df.update(merged_df.filter(like='_Rate').ffill())
#
# # Drop unnecessary columns
# merged_df.drop(columns=date_columns_stock[0], inplace=True)
#
# # Reorder columns as needed
# # merged_df = merged_df[['Date', 'Other Columns Here']]
# # Handle missing values
# merged_df.fillna(0, inplace=True)  # Replace NaN with 0
#
# # # Convert date column to datetime object
# # merged_df['Date'] = pd.to_datetime(df['Date'])
