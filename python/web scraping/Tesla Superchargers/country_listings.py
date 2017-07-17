# pylint: disable=invalid-name
# pylint: disable=C0111

import csv
import requests
from bs4 import BeautifulSoup
import tsc_profile

"""
Scrapes the United States listings of Tesla Superchargers for each profile page
"""

def getListing(url):
    print("Scraping listings from:", url)

        # Check response status
    r = requests.get(url)
    if r.status_code == 200:

        # Parse response
        soup = BeautifulSoup(r.content, 'lxml')
        section = soup.find('section', {'class': 'find-us-list-state'})

        a_tags = section.select('a')

        url_list = []

        for a in a_tags:
            url_list.append(a['href'])

        return url_list

    else:
        print("Request:", url, "failed with code:", r.status_code)
        r.close()


def main():
    """Module driver"""
    # URLs = [r'https://www.tesla.com/findus/list/superchargers/United+States',
    #         r'https://www.tesla.com/findus/list/superchargers/Canada',
    #         r'https://www.tesla.com/findus/list/superchargers/China']

    URLs = [r'https://www.tesla.com/findus/list/superchargers/United+States']

    profile_urls = []

    for url in URLs:
        profile_urls.extend(getListing(url))

    with open(r'C:\data\superchargers.csv', mode='w', newline='') as csvfile:
        fieldnames = ['coming_soon', 'name', 'address_name', 'street_address',
                      'extended_address', 'locality', 'map_url', 'dir_url', 'num_chargers']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for profile in profile_urls:
            writer.writerow(tsc_profile.getProfile(profile))

    print("Done!")

if __name__ == "__main__":
    main()
