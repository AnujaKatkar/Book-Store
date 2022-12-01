#Script - createCountries
import csv

def create():
    data_dir = './Data_Files/'
    list_countries = ['USA', 'UK', 'Egypt', 'India', 'Nepal', 'Australia', 'Singapore', 'Argentina',
                    'Brazil', 'Spain', 'France', 'Peru', 'Ghana', 'Canada', 'Japan', 'Chile', 'Germany']

    f = open(f'{data_dir}countries.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['CountryName']
    writer.writerow(row)

    for i in range(1, len(list_countries)+1):
        cID = i
        cName = list_countries[i-1]
        row = [cName]
        writer.writerow(row)
