
# pylint: disable=C0103

import csv
import requests as r
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

url = 'https://www.concretedisciples.com'

with open(r'c:\data\park_urls.csv', 'w', newline='') as csvfile:
    fieldnames = ['park_name', 'park_url']
    writer = csv.DictWriter(csvfile, fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for i in range(1, 3):
        # request page; make soup; close page
        print("Scraping...", url + "&page=" + str(i))
        page = r.get(url, params={'limit': 50, 'page': i})
        soup = bs(page.content, 'html.parser')
        page.close()

        # create list or urls
        park_dict = {}

        for e in tqdm(soup.find_all('div', {'class': 'jrContentTitle'})):
            # park_name = e.a.string
            park_url = e.a['href']

            # make profile soup
            profile_page = r.get(url + park_url)
            profile_soup = bs(profile_page.content, 'html.parser')
            profile_page.close()

            # skateparkname
            park_name_tag = profile_soup.find('div', {'class': 'jrFieldRow jrSkateparkname'})
            if park_name_tag is not None:
                park_name = park_name_tag.contents[-1].string

            # extract general
            # bmx
            # openclosed
            # lights
            # restrooms
            # rip
            # freepay
            # indoors
            # padsrequired
            # surface
            # proshop

            # extract construction

            # extract location
            # address
            # postal code
            # city

            # extract contacts
            # management

            # write data
            writer.writerow({'park_name': park_name, 'park_url': park_url})

        print()

# with open(r'c:\data\park_urls.csv', 'w') as csvfile:
#     fieldnames = ['park_url']
#     # writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#     writer = csv.DictWriter(csvfile, fieldnames)

    # writer.writerow(fieldnames)
    # writer.writeheader()

    # for row in park_dict:
    #     writer.writerow(row)
