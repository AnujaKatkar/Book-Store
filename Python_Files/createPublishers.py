# Script 2 - Table Publishers
# columns - PublicationID, PublicationName, Country
import csv
import random

def create():
    data_dir = './Data_Files/'
    f = open(f'{data_dir}publications.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['PublicationName'] + ['CountryID']
    writer.writerow(row)

    namePrefix = "Publication Num"

    for i in range(1, 51):
        pID = i
        pName = namePrefix + str(i)
        pCountry = random.randint(1, 17)
        row = [pName] + [pCountry]
        writer.writerow(row)
