import csv
import requests

DATA_LOCATION = '../data/owid-covid-latest.csv'
URL = 'https://github.com/owid/covid-19-data/raw/master/public/data/latest/owid-covid-latest.csv'

with open(DATA_LOCATION) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row['location'], row['total_cases'])


def csv_getter(url):
    r = requests.get(url)
    decoded_content = r.content.decode('utf-8')
    return decoded_content.splitlines()
