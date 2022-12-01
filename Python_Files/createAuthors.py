# Script 1 - Table Authors
# columns - AuthorID, #AuthorName
import csv

def create():
    data_dir = './Data_Files/'
    f = open(f'{data_dir}authors.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['AuthorName']
    writer.writerow(row)

    namePrefix = "Author Num"

    for i in range(1, 201):
        authorName = namePrefix + str(i)
        row = [authorName]
        writer.writerow(row)
