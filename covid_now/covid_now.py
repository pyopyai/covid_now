import csv
import requests
from operator import itemgetter

DATA_LOCATION = '/tmp/covid_now/owid-covid-latest.csv'
URL = 'https://github.com/owid/covid-19-data/raw/master/public/data/latest/owid-covid-latest.csv'


# with open(DATA_LOCATION) as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row['location'], row['total_cases'])


def csv_getter(url):
    r = requests.get(url)
    decoded_content = r.content.decode('utf-8')
    return decoded_content.splitlines()


def show_graph(csv_data):
    reader = csv.DictReader(csv_data, delimiter=',', quotechar='"')
    graph_data = list()
    for row in reader:
        try:
            graph_data.append([row['location'], float(row['total_cases'])])
        except ValueError:
            graph_data.append([row['location'], 0])

    graph_data.sort(key=itemgetter(1))
    print(graph_data)


show_graph(csv_getter(URL))
