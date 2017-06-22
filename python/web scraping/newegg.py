
# Introduction to Web Scraping (with Python and BeautifulSoup)
# https://www.youtube.com/watch?v=XQgXKtPSzUI

from urllib.request import urlopen as uReq  # import urlopen function from urllib package and request module, aliasing as 'uReq'
from bs4 import BeautifulSoup as soup       # importing the BeautifulSoup module from bs4 package and aliasing as 'soup'

# home url
my_url = 'https://www.newegg.com/UltraWide-Monitors/PromotionStore/ID-736?cm_sp=CAT_Monitors-_-VisNav_4-_-UltraWide-Monitors_1'

# opening conection; request page; capture response as http.client.HTTPResponse
uClient = uReq(my_url)

# read respsonse text as string
page_html = uClient.read()

# close connection
uClient.close()

# use BeautifulSoup to parse HTML
page_soup = soup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("div", {"class":"item-container"})

# open file; write headers
filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

# loop through containers collecting data
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    price_ship = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product: " + product_name)
    print("shipping: " + price_ship)

    f.write("\"" + brand + "\" , \"" + product_name.replace("\"", r"\"") + "\", \"" + price_ship + "\"\n")

f.close()
