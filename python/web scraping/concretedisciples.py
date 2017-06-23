#!/usr/bin/env python

# pylint: disable=C0103

# TODO: Use command line arguments for starting URL and number of pages
# TODO: Performance tune
# TODO: Error handling

import csv
import requests as r
from bs4 import BeautifulSoup as bs
from tqdm import tqdm


# url = 'https://www.concretedisciples.com'
base_url = 'https://www.concretedisciples.com'
url = 'https://www.concretedisciples.com/skatepark-directory/usa-skateparks'
headers = headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) ' +
                   'AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 ' +
                   'Safari/600.1.4'}

def main():
    """
    Scrapes the concretedisciples.com site for every park and it's metadata.

    Eric Bragas 2017.6.22
    """
    # open file for writing
    with open(r'c:\data\park_urls.csv', 'w', newline='') as csvfile:
        fieldnames = ['park_name', 'park_url', 'bmx', 'rip', 'lights', 'restrooms', 'freepay',
                      'indoors', 'pads', 'surface', 'proshop', 'address', 'zipcode', 'city',
                      'management', 'description']

        writer = csv.DictWriter(csvfile, fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        # start loading list pages
        for i in range(1, 2):
            print("Scraping...", url + "?page=" + str(i) + "&limit=50")
            page = r.get(url, params={'limit': 50, 'page': i}, headers=headers)
            soup = bs(page.content, 'html.parser')
            page.close()

            # traverse and extract each profile
            for e in tqdm(soup.find_all('div', {'class': 'jrContentTitle'})):
                park_url = e.a['href']
                profile_page = r.get(base_url + park_url)
                profile_soup = bs(profile_page.content, 'html.parser')
                profile_page.close()

                # parse page for variables
                park_name = profile_get(profile_soup, 'jrFieldRow jrSkateparkname')
                bmx = profile_get(profile_soup, 'jrFieldRow jrBmx')
                rip = profile_get(profile_soup, 'jrFieldRow jrRip')
                lights = profile_get(profile_soup, 'jrFieldRow jrLightsx')
                restrooms = profile_get(profile_soup, 'jrFieldRow jrRestroomsx')
                freepay = profile_get(profile_soup, 'jrFieldRow jrFreepayx')
                indoors = profile_get(profile_soup, 'jrFieldRow jrIndoorsx')
                pads = profile_get(profile_soup, 'jrFieldRow jrPadsx')
                surface = profile_get(profile_soup, 'jrFieldRow jrSurfacex')
                proshop = profile_get(profile_soup, 'jrFieldRow jrProshopx')
                address = profile_get(profile_soup, 'jrFieldRow jrAddress')
                zipcode = profile_get(profile_soup, 'jrFieldRow jrZip')
                city = profile_get(profile_soup, 'jrFieldRow jrCity')
                management = profile_get(profile_soup, 'jrFieldRow jrManagement')

                desc_tag = profile_soup.find('div', {'class': 'jrListingFulltext '}).find('p')
                description = desc_tag.text if desc_tag is not None else None
                # soup.find('div', {'class': 'jrListingFulltext'}).find('p').text

                # write data
                writer.writerow({'park_name': park_name,
                                 'park_url': park_url,
                                 'bmx': bmx,
                                 'rip': rip,
                                 'lights': lights,
                                 'restrooms': restrooms,
                                 'freepay': freepay,
                                 'indoors': indoors,
                                 'pads': pads,
                                 'surface': surface,
                                 'proshop': proshop,
                                 'address': address,
                                 'zipcode': zipcode,
                                 'city': city,
                                 'management': management,
                                 'description': description})

            print()



def profile_get(soup, pName, tType='div', pType='class'):
    """
    soup: BeautifulSoup object
    tType: string, type of tag eg. div, a, etc.; default 'div'
    pType: string, property type eg. class, id, etc.; default 'class'
    pName: string property name

    Returns string from last element in contents of tag if tag exists, else None
    """
    tag = soup.find(tType, {pType, pName})
    value = tag.contents[-1].string if tag is not None else None

    return value



if __name__ == "__main__":
    main()
