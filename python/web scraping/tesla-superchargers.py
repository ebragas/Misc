
import requests
import csv
from bs4 import BeautifulSoup

URL = r'https://www.tesla.com/findus/list/superchargers/United+States'

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'lxml')
r.close()

states = soup.find_all('div', {'class': 'state'})

len(states)
for i in states:
    print(i.h2.text)

data = []
row = {}

for state in states:
    
    for card in state.find_all('address', {'class': 'vcard'}):
        row['state'] = state.h2.text
        row['name'] = card.a.text
        row['url'] = card.a['href']
        row['street-address'] = card.find('span', {'class': 'street-address'}).text
        row['extended-address'] = card.find('span', {'class': 'extended-address'}).text
        row['locality'] = card.find('span', {'class': 'locality'}).text
#         print(row)
        data.append(row.copy())
#         print(data[-1])
        
print(data)
print(len(data))

fieldnames = ['state', 'name','url', 'street-address', 'extended-address', 'locality']

with open('c:\data\superchargers.csv', mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for r in data:
        writer.writerow(r)
