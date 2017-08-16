
import csv
import googlemaps
from datetime import datetime

SOURCE_FILE = r'C:\data\skate-parks\ccd.csv'
# SOURCE_FILE = r'C:\data\skate-parks\ccd_sample_error.csv'
DEST_FILE = r'C:\data\skate-parks\ccd_20170815.csv'
KEY = 'AIzaSyCq-NNfZ6knfLR56b2XlTiILMMOyt2y534'

def main():
    start_time = datetime.now()

    # Start Google Maps Client
    gmaps = googlemaps.Client(key=KEY)

    # Read source file
    infile = open(SOURCE_FILE, mode='r', encoding='utf-8')
    reader = csv.DictReader(infile)

    fieldnames = list(reader.fieldnames)
    fieldnames.extend(['formatted_address', 'lat', 'lng', 'location_type'])

    # Destination file
    outfile = open(DEST_FILE, mode='w', newline='', encoding='utf8')
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quotechar='"')
    writer.writeheader()

    # Read line, geocode, write line
    for row in reader:

        # Geocode location
        row['country'] = ' '.join(row['country'].split(' ')[:-1])
        location = ' '.join([row['address'], row['city'], row['zipcode'], row['country']]).strip()

        # Geocode address
        result = gmaps.geocode(location)
        try:
            row['formatted_address'] = result[0]['formatted_address']
            row['lat'] = result[0]['geometry']['location']['lat']
            row['lng'] = result[0]['geometry']['location']['lng']
            row['location_type'] = result[0]['geometry']['location_type']
            writer.writerow(row)
        except IndexError:
            row['location_type'] = "NO RESULT"
            writer.writerow(row)

        print(location, ':', row['location_type'])

    # Close files
    infile.close()
    outfile.close()

    print("\nTotal Runtime: {}".format(str(datetime.now() - start_time)))

if __name__ == "__main__":
    main()
