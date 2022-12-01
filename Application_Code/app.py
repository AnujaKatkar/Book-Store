import streamlit as stream
stream.set_page_config(layout="wide")

from multiplefiles import MultipleFiles
from Files import mainpage,view, advanced_queries

app = MultipleFiles()

stream.title("Bookstore")
app.add_page("Home", mainpage.run)
app.add_page("View", view.run)
app.add_page("Advanced Queries",advanced_queries.run)

app.run()







