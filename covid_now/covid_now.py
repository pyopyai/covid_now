import csv

with open('../data/owid-covid-latest.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',',quotechar='"')
    for row in reader:
        print(row['location'],row['total_cases'])
