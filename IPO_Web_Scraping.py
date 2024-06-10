# import yfinance as yf
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# def get_ticker_symbol(ipo_name):
#     try:
#         # Search for the stock using yfinance
#         search_result = yf.Ticker(ipo_name)
#         if search_result:
#             # Get the ticker symbol
#             return search_result.info['symbol']
#     except Exception as e:
#         print(f"Could not retrieve ticker for {ipo_name}: {e}")
#     return None
#
# def get_upcoming_ipos_with_tickers():
#     url = 'https://ticker.finology.in/IPO/listed'  # Update with the actual URL
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         ipo_names = []
#
#         # Find all cards with the class 'cardscreen'
#         cards = soup.find_all(class_='card')
#
#         # Extract IPO names
#         for card in cards:
#             # Get IPO name if available
#             complink_elem = card.find(class_='complink')
#             if complink_elem:
#                 ipo_name = complink_elem.text.strip()
#                 ipo_names.append(ipo_name)
#
#         return ipo_names
#
# # Get the upcoming IPO names
# upcoming_ipo_names = get_upcoming_ipos_with_tickers()
#
# # Initialize DataFrame
# df = pd.DataFrame({'IPO Name': upcoming_ipo_names})
#
# # Add a column for ticker symbols
# df['Ticker Symbol'] = df['IPO Name'].apply(get_ticker_symbol)
#
# # Save the DataFrame to an Excel file
# df.to_excel('upcoming_ipos_with_tickers.xlsx', index=False)
#
# print("D
# ata has been saved to 'upcoming_ipos_with_tickers.xlsx'")


# import pandas as pd
# import requests
# import time
#
# # Your Alpha Vantage API key
# api_key = '32Y7TBM8X346ZVGY'
#
# # List of company names
# companies = [
#     "Rainbow Children's Medicare Ltd.", "Campus Activewear Ltd.", "Hariom Pipe Industries Ltd.",
#     "Veranda Learning Solutions Ltd.", "Uma Exports Ltd.", "Vedant Fashions Ltd.",
#     "Adani Wilmar Ltd.", "AGS Transact Technologies Ltd.", "CMS Info Systems Ltd.",
#     "Supriya Lifescience Ltd.", "HP Adhesives Ltd."
# ]
#
#
#
# # Function to get the ticker symbol using Alpha Vantage
# def get_ticker_symbol(company_name, api_key):
#     url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}'
#     response = requests.get(url)
#     time.sleep(12)  # Add delay to avoid rate limits
#     data = response.json()
#
#     if 'bestMatches' in data:
#         return data['bestMatches'][0]['1. symbol']
#     return None
#
#
# # Create a dataframe to store company names and their ticker symbols
# df = pd.DataFrame(companies, columns=['Company'])
# df['Ticker'] = df['Company'].apply(lambda x: get_ticker_symbol(x, api_key))
#
# # Display the dataframe
# print(df)



import nsepython

# Print out all the available attributes and functions in nsepython
print(dir(nsepython))


# Example usage of a hypothetical function
company_name = "Reliance Industries"

# Function to get ticker name by company name
def get_ticker_by_company_name(company_name):
    # Replace this with the correct function from nsepython after inspection
    search_results = nsepython.some_search_function(company_name)
    if search_results and 'data' in search_results:
        for result in search_results['data']:
            if result['companyName'].lower() == company_name.lower():
                return result['symbol']
    return None

# Example usage
ticker_name = get_ticker_by_company_name(company_name)
if ticker_name:
    print(f"The ticker name for {company_name} is {ticker_name}")
else:
    print(f"Ticker name for {company_name} not found")
