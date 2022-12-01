import streamlit as stream
stream.set_page_config(layout="wide")

from multiplefiles import MultipleFiles
from Files import mainpage,view, table_joins

app = MultipleFiles()

stream.title("Bookstore")
app.add_page("Home", mainpage.run)
app.add_page("Query Table", view.run)
app.add_page("Table Joins",table_joins.run)

app.run()







