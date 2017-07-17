# Tesla Supercharger Web Scraping

Web scrapes the Tesla Supercharger listings and profiles pages for data, such as: address, name, GoogleMaps static image URL, and writes data to CSV.

## Getting Started

To install, place the `scrape_chargers.py` and `tsc_profile.py` files in the desired directory and execute the following command to use the default configurations:

```
C:\>python scrape_chargers.py
```

Open and edit the `scrape_chargers.py` Python file to change the default configurations such as the file location to write output data to, and the listings URLs to iterate over and scrape.

### Prerequisites

The project uses Python 3.6.0 and the Requests and BeautifulSoup packages.

```python
>>> pip install requests
>>> pip install  beautifulsoup4
```