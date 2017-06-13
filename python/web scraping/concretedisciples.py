
# import modules
import requests
from bs4 import BeautifulSoup as bs
import csv
import time

# start msg
print('Starting.')

# base url: https://www.concretedisciples.com/?limit=50&page=192
start_url = 'https://www.concretedisciples.com/'
url_params = {'limit': 50, 'page': 1}

# init park urls list
park_urls = []

# pages loop
for i in range(5):  # 192
    url_params['page'] = i + 1

    # request page
    print('Requesting...', start_url + '?limit=' + str(url_params['limit']) +
        '&page=' + str(url_params['page']))
    page = requests.get(start_url, url_params)

    soup = bs(page.text, 'html.parser')

    for link in soup.find_all('a'):
        print(link.text)

    page.close()

    # time.sleep(1)
