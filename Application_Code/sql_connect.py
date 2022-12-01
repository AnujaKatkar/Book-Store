import psycopg2
# from Application_Code.ERP_System import config
# import config

connection = psycopg2.connect(
    host="127.0.0.1",
    database="Project_Bookstore",
    user="postgres",
    password="postgres@98")

connection.autocommit = True
current = connection.cursor()