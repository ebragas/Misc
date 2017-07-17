# pylint: disable=invalid-name
# pylint: disable=C0111

import requests
from bs4 import BeautifulSoup

def getProfile(url):
    """
    Input: url, url of Tesla Supercharger profile page
    Returns dictionary of available data points
    """
    url = r'https://www.tesla.com' + url
    print(url)  # testing
    data = {}

    # Request profile and check for success
    r = requests.get(url)
    if r.status_code == 200:

        # Parse response
        soup = BeautifulSoup(r.text, 'lxml')
        r.close()

        # Coming soon
        if soup.find('span', {'class': 'coming-soon'}):
            data['coming_soon'] = soup.find('span', {'class': 'coming-soon'}).text
        else:
            data['coming_soon'] = 'Open'

        # print(data['coming_soon'])

        # Name
        h1 = soup.find_all('h1')
        data['name'] = h1[-1].text
        # print(data['name'])  # testing

        # Address name
        data['address_name'] = soup.find('span', {'class': 'common-name'}).text
        # print(data['address_name']) # testing

        # Street address
        data['street_address'] = soup.find('span', {'class': 'street-address'}).text
        # print(data['street_address']) # testing

        # Extended address
        data['extended_address'] = soup.find('span', {'class': 'extended-address'}).text
        # print(data['extended_address']) # testing

        # Locality
        data['locality'] = soup.find('span', {'class': 'locality'}).text
        # print(data['locality']) # testing

        # Map URL
        data['map_url'] = soup.find('div', {'id': 'location-map'}).a.img['src']
        # data['map_url'] = div_map.a.img['src']
        # print(data['map_url'])  # testing

        # Directions URL
        if soup.find('a', {'class': 'directions-link'}):
            data['dir_url'] = soup.find('a', {'class': 'directions-link'})['href']
            # print(data['dir_url'])  # testing

        # Num_Chargers
        data['num_chargers'] = soup.select('p:nth-of-type(2)')[0].contents[-1]
        # print(data['num_chargers'])  # testing


    # Exit gracefully
    else:
        print("Request:", url, "failed with code:", r.status_code)
        r.close()

    return data

def main():
    """Module driver"""
    profile_urls = [r'https://www.tesla.com/findus/location/supercharger/athensalsupercharger',
                    r'https://www.tesla.com/findus/location/supercharger/paysonsupercharger',
                    r'https://www.tesla.com/findus/location/supercharger/elcentrosupercharger']

    for url in profile_urls:
        getProfile(url)

    print("Done!")

if __name__ == "__main__":
    main()
