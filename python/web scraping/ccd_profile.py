# pylint: disable=invalid-name

# break down the profile page parsing into a single function


from datetime import datetime
import requests
from bs4 import BeautifulSoup

# constants
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) ' +
                         'AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 ' +
                         'Safari/600.1.4'}


# retrieves data from a park profile page
def profile_get(url):
    """
    url: string url for the concretedisciples page to parse
    Returns a dictionary of the fields and values available on the profile.
    """

    print("Requesting...", url)
    r = requests.get(url)

    if r.status_code == 200:
        print("Processing...")
        soup = BeautifulSoup(r.text, 'lxml')
        r.close()

        field_tags = soup.select(".jrFieldLabel")
        value_tags = soup.select(".jrFieldValue ")

        fields = []
        values = []

        for t in field_tags:
            fields.append(t.text.strip())

        for t in value_tags:
            values.append(t.text.strip())

        data = dict(zip(fields, values))

        return data

    else:
        print(r.status_code)
        r.close()

    print("Done!")


# Retrieves a list of URLs from a listings page
def urllist_get(url, size):
    """
    ...
    """
    print("Retrieving URLs...")
    r = requests.get(url + "/?limit=" + str(size))
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        r.close()

        urllist = []
        for tag in soup.select(".jrContentTitle"):
            urllist.append(tag.a['href'])

        return urllist

    else:
        print(r.status_code)
        r.close()


url = 'https://www.concretedisciples.com'

urls = urllist_get(url, 50)

# Get list of available fields
# fields_list = []
# for i in urls:
#     for j in profile_get(url + i).keys():
#         if j not in fields_list:
#             fields_list.append(j)

# for k in fields_list:
#     print(k)
