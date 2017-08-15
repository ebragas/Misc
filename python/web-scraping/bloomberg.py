
print('Starting...')

# import modules
import urllib.request as ureq  # not urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

quote_page = ['https://www.bloomberg.com/quote/SPX:IND', 'https://www.bloomberg.com/quote/CCMP:IND', 'https://www.bloomberg.com/quote/INDU:IND']

# create dictionary
# data = {}s
data = []

# loop through pages
for pg in quote_page:

    # request page
    print('Requesting page...', pg)
    page = ureq.urlopen(pg)

    # parse page html using BeautifulSoup
    print('Parsing page...')
    soup = BeautifulSoup(page, 'html.parser')

    # close page
    print('Closing page...')
    page.close()

    # extract index name
    name_box = soup.find('h1', attrs={'class': 'name'})
    # data['name'] = name_box.text.strip()
    name = name_box.text.strip()

    # extract index price
    price_box = soup.find('div', attrs={'class': 'price'})
    # data['price'] = price_box.text.strip()
    price = price_box.text.strip()

    # extract ticker
    ticker_box = soup.find('div', attrs={'class': 'ticker'})
    # data['ticker'] = ticker_box.text.strip()
    ticker = ticker_box.text.strip()

    # extract price datetime
    # date_box = soup.find('div', attrs={'class': 'price_datetime'})
    # data['price_date'] = date_box.text.strip()
    # price_date = date_box.text.strip()

    # add current date to dictionary
    # data['date'] = datetime.now()

    # save data in tuple
    # data.append((name, ticker, price, price_date, date))
    data.append((name, ticker, price))

# append to csv
filename = 'c:/data/bloomberg_stocks.csv'
print('Writing to...', filename)

with open(filename, 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, ticker, price in data:
        writer.writerow([name, ticker, price, datetime.now()])

print('Done.')
