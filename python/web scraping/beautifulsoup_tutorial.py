
# pylint: disable=C0103

import csv
import requests as r
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


url = 'https://www.concretedisciples.com'

def main():
    # open file for writing
    with open(r'c:\data\park_urls.csv', 'w', newline='') as csvfile:
        fieldnames = ['park_name', 'park_url', 'bmx', 'rip', 'lights', 'restrooms', 'freepay',
                    'indoors', 'pads']
        writer = csv.DictWriter(csvfile, fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        # start loading list pages
        for i in range(1, 2):
            print("Scraping...", url + "?page=" + str(i))
            page = r.get(url, params={'limit': 50, 'page': i})
            soup = bs(page.content, 'html.parser')
            page.close()

            # create list of urls
            park_dict = {}

            # traverse and extract each profile
            for e in tqdm(soup.find_all('div', {'class': 'jrContentTitle'})):
                park_url = e.a['href']
                profile_page = r.get(url + park_url)
                profile_soup = bs(profile_page.content, 'html.parser')
                profile_page.close()

                # skateparkname
                park_name_tag = profile_soup.find('div', {'class': 'jrFieldRow jrSkateparkname'})
                park_name = park_name_tag.contents[-1].string if park_name_tag is not None else None

                # bmx
                bmx_tag = profile_soup.find('div', {'class': 'jrFieldRow jrBmx'})
                bmx = bmx_tag.contents[-1].string if bmx_tag is not None else None

                # rip
                rip_tag = profile_soup.find('div', {'class': 'jrFieldRow jrRip'})
                rip = rip_tag.contents[-1].string if rip_tag is not None else None

                # lights
                lights_tag = profile_soup.find('div', {'class': 'jrFieldRow jrLightsx'})
                lights = lights_tag.contents[-1].string if lights_tag is not None else None

                # restrooms
                restrooms_tag = profile_soup.find('div', {'class': 'jrFieldRow jrRestroomsx'})
                restrooms = restrooms_tag.contents[-1].string if restrooms_tag is not None else None

                # freepay
                freepay_tag = profile_soup.find('div', {'class': 'jrFieldRow jrFreepayx'})
                freepay = freepay_tag.contents[-1].string if freepay_tag is not None else None

                # indoors
                indoors_tag = profile_soup.find('div', {'class': 'jrFieldRow jrIndoorsx'})
                indoors = indoors_tag.contents[-1].string if indoors_tag is not None else None

                # padsrequired
                pads = profile_get(soup=profile_soup, tType='div', pType='class',
                                   pName='jrFieldRow jrPadsx')

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
                writer.writerow({'park_name': park_name, 'park_url': park_url, 'bmx': bmx,
                                 'rip': rip, 'lights': lights, 'restrooms': restrooms,
                                 'freepay': freepay, 'indoors': indoors, 'pads': pads})

            print()



def profile_get(soup, tType, pType, pName):
    """
    soup: BeautifulSoup object
    tType: string, type of tag eg. div, a, etc.
    pType: string, property type eg. class, id, etc.
    pName: string property name

    Returns string from last element in contents of tag if tag exists, else None
    """
    tag = soup.find(tType, {pType, pName})
    value = tag.contents[-1].string if tag is not None else None
    
    return value



if __name__ == "__main__":
    main()