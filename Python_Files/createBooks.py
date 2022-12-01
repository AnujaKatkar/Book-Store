# script 3 - Table Books
#columns - bookID, authorID, publicationID, title, genre, publicationYear, price, numRemaining
import csv
import random


def create():
    data_dir = './Data_Files/'
    f = open(f'{data_dir}books.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    row = ['AuthorID'] + ['PublicationID'] + ['Title'] + \
        ['Genre'] + ['PublicationYear'] + ['Price']
    writer.writerow(row)
    list_genres = ['Fiction', 'Mystery', 'Thriller', 'Horror',
                'Historical', 'Western', 'Comic', 'Children']
    num_genres = len(list_genres)
    namePrefix = "BookNum"

    for i in range(1, 20001):
        aID = (random.randint(1, 50))
        pID = (random.randint(1, 20))
        title = namePrefix + str(i)
        genre = list_genres[random.randint(0, num_genres-1)]
        publicationYear = random.randint(1800, 2022)
        price = random.randint(20, 2000)
        row = [aID] + [pID] + [title] + [genre] + \
            [publicationYear] + [price]
        writer.writerow(row)
