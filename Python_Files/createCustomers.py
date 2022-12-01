# Script 4 - Table Customers
# columns - customerID, customerName, address, phoneNo, postalCode
import csv
import random

def create():
    data_dir = './Data_Files/'
    f = open(f'{data_dir}customers.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['CustomerName'] + \
        ['Address'] + ['PhoneNumber'] + ['PostalCode']
    writer.writerow(row)

    streets = ['Main St', 'Montrose Ave', 'Englewood Ave', 'Merrimac St',
            'University Ave', 'Flower St', 'Winspear Ave', 'Callodine St']
    states = ['New York', 'Boston', 'California', 'Iowa', 'Arizona',
            'Washington', 'New Jersey', 'Florida', 'Delaware', 'Maryland', 'Virginia']

    numStreets = len(streets)
    numStates = len(states)

    namePrefix = "Customer Num"

    for i in range(1, 20001):
        cName = namePrefix + str(i)
        address = str(random.randint(1, 3000)) + ' ' + streets[random.randint(
            0, numStreets-1)] + ', ' + states[random.randint(0, numStates-1)]
        phoneNo = random.randint(7000000000, 9999999999)
        postalCode = random.randint(1, 99950)
        row = [cName] + [address] + [phoneNo] + [postalCode]
        writer.writerow(row)
