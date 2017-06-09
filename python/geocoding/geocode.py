# Geocode skate parks based on addresses

# TODO:
# * open file
# * read line
# * loop through file
# * pass address to geocoding method
# * parse result
# * store result data and original data in csv file

import googlemaps

print('Off to a good start!')

# open file
filename = r'C:\data\skate parks\ccd-texas-attributes.txt'
infile = open(filename, 'r')

headers = infile.readline()
headers = headers.split('\t')

# open googlemaps client
gmaps = googlemaps.Client(key='AIzaSyDRscrs5Wjz-OTlHpIa-wC1eg5tolmEu7Q')

for line in infile:

    # read and parse line
    l = infile.readline()
    l = l.split('\t')

    # address parts
    if len(l) >= 15:
        address = l[12]
        postal_code = l[13]
        city = l[14]
        state = l[0]

        location = address + ' ' + city + ' ' + state + ' ' + postal_code + ' '

        geocode_result = gmaps.geocode(location)
        print(geocode_result)

infile.close()
