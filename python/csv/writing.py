
# CSV file module testing
# documentation: https://docs.python.org/3/library/csv.html

# pylint: disable=C0103

"""
Test driving the functions provided by the CSV module
"""

import csv

# csv.writer
with open(r'c:\data\trash\eggs.csv', mode='w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=', ',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            # csv.QUOTE_MINIMAL is a module variable
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



# csv.DictReader
with open(r'c:\data\trash\names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first'], row[' last'])



# csv.DictWriter
with open(r'c:\data\trash\names.csv', mode='w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
