import requests
from bs4 import BeautifulSoup

def scrape_indian_ipo_details():
    url = "https://www.moneycontrol.com/ipo/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    ipo_details = []

    # Find IPO details from the website
    ipo_cards = soup.find_all('div', class_='ipo_listing')
    for card in ipo_cards:
        name = card.find('h2', class_='company_name').text.strip()
        price = card.find('div', class_='price_block').text.strip()
        date = card.find('div', class_='ipo_listing_date').text.strip()
        ipo_details.append({'Name': name, 'Price': price, 'Date': date})

    return ipo_details

def main():
    ipo_details = scrape_indian_ipo_details()
    for idx, ipo in enumerate(ipo_details, start=1):
        print(f"IPO #{idx}:")
        print("Name:", ipo['Name'])
        print("Price:", ipo['Price'])
        print("Date:", ipo['Date'])
        print()

if __name__ == "__main__":
    main()
