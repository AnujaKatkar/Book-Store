import psycopg2
import pandas as pd
import numpy as np
import glob

conn = psycopg2.connect(
    host="localhost",
    database="Bookstore",
    user="postgres",
    password="postgres@98")

cur = conn.cursor()

data_dir = './Data_Files/'

tables = ['authors', 'countries', 'publications', 'books', 'customers', 'orders', 'orderDetails']

for table in tables[::-1]:
    sql = f"DROP TABLE {table};"
    cur.execute(sql)
    conn.commit()

cur.execute(open("./SQL_Files/create.sql", "r").read())
conn.commit()

for table in tables:
    print(f"Inserting values into table {table}")
    path = f"{data_dir}{table}.csv"
    df = pd.read_csv(path)

    length, column_names = df.shape[1], df.columns.values

    df = df.fillna(np.nan)
    df = df.replace([np.nan], [None])

    columns = ",".join([col for col in column_names])
    holder = ("%s," * length).rstrip(",")

    sql = f"INSERT INTO {table} ({columns}) VALUES ({holder});"
    data = df.values.tolist()
    cur.executemany(sql, data)
    conn.commit()