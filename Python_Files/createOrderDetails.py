# Script 6 - Table OrderDetails
# colimns - OrderID, BookID, Price
import csv
import random

def create():
    data_dir = './Data_Files/'
    f = open(f'{data_dir}orderDetails.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['OrderID'] + ['BookID'] + ['Price']
    writer.writerow(row)

    csvfile = open(f'{data_dir}books.csv', newline='')
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = 0
    tuples = []
    for row in reader:
        count += 1
        tuples.append(row[0].split(","))
    tuples.pop(0)
    count -= 1

    mapData = {}

    for i in range(1, 25001):
        oID = i
        bookInfo = random.randint(1, count)
        bID = bookInfo
        price = tuples[bookInfo-1][5]
        row = [oID] + [bID] + [price]
        mapData[oID] = []
        mapData[oID].append(bookInfo)
        writer.writerow(row)

    for i in range(25002, 100000):
        oID = random.randint(1, 25000)
        bookInfo = random.randint(1, count)
        if oID in mapData:
            while bookInfo in mapData[oID]:
                bookInfo = (bookInfo + 50) % count
            mapData[oID].append(bookInfo)
        else:
            mapData[oID] = []
            mapData[oID].append(bookInfo)
        
        bID = bookInfo
        price = tuples[bookInfo-1][5]
        row = [oID] + [bID] + [price]
        writer.writerow(row)
