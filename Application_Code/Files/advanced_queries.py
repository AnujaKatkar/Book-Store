import streamlit as stream
from sql_connect import cursor
import pandas as pd
def run():
    different_joins = ['Publication Averages Per Book', 'Books Per Author','Price Per Author', 'Top Countries Authors and Books']

    selected_join =stream.sidebar.selectbox("Select Use Case", different_joins) #on_change= reset_page_function)

    if selected_join == 'Publication Averages Per Book':
        display_papb()
    
    elif selected_join == 'Books Per Author':
        display_bpa()
    
    elif selected_join == 'Price Per Author':
        display_ppa()

    elif selected_join == 'Top Countries Authors and Books':
        display_tcab()

def display_tcab():
    # if 'pg_num' not in stream.session_state:
    #    stream.session_state.pg_num = 0
    sql = f"""SELECT
	books.*
FROM (
	SELECT
		countries.countryid AS cid,
		count(publications.PublicationName) AS pub_count
	FROM
		publications,
		countries
	WHERE
		publications.CountryID = countries.countryid
	GROUP BY
		countries.countryid
	ORDER BY
		pub_count DESC
	LIMIT 1) AS join1,
	publications,
	books
WHERE
	publications.countryid = join1.cid
	AND books.publicationid = publications.publicationid"""
    stream.code(f"Executed Query: \n{sql}", language='sql')
    cursor.execute(sql)
    colnames = [desc[0] for desc in cursor.description]
    result = cursor.fetchall()
    result = pd.DataFrame(result, columns=colnames)
    stream.dataframe(result, use_container_width=True)
    # n = 30
    # if(len(result) > 30):
    #     prev, _ ,next = stream.columns([1.7, 10, 1.5])
    #     if next.button("Next"):
    #         if stream.session_state.pg_num + 1 > len(result) // n:
    #            stream.session_state.pg_num = 0
    #         else:
    #            stream.session_state.pg_num += 1

    #     if prev.button("Previous"):

    #         if stream.session_state.pg_num - 1 < 0:
    #            stream.session_state.pg_num = len(result) // n
    #         else:
    #            stream.session_state.pg_num -= 1
    # if(len(result) > 30):
    #     display_df = result.iloc[stream.session_state.cursor.fetchall() * n :(1 +stream.session_state.pg_num) * n]
    #     stream.table(display_df)
    # else:
    #     stream.table(result)

def display_papb():
    # if 'page_number' not in stream.session_state:
    #    stream.session_state.pg_num = 0
    sql = f"""SELECT
    publications.publicationname AS PublicationName,
    sum(books.price) / count(books.bookid) AS AveragePrice
FROM
    books,
    publications
WHERE
    books.publicationid = publications.publicationid
GROUP BY
    publications.publicationname"""
    stream.code(f"Executed Query: \n{sql}", language='sql')
    cursor.execute(sql)
    
    column_names = [col[0] for col in cursor.description]
    final_result = pd.DataFrame(cursor.fetchall(), columns=column_names)
    stream.dataframe(final_result, use_container_width=True)

def display_bpa():
    # if 'pg_num' not in stream.session_state:
    #    stream.session_state.pg_num = 0
    sql = f"""SELECT
    authors.authorname AS AuthorName,
    count(books) AS NumberOfBooks
FROM
    books,
    authors
WHERE
    books.authorid = authors.authorid
GROUP BY
    authors.authorid"""
    stream.code(f"Executed Query: \n{sql}", language='sql')
    cursor.execute(sql)
    
    column_names = [col[0] for col in cursor.description]
    final_result = pd.DataFrame(cursor.fetchall(), columns=column_names)
    stream.dataframe(final_result, use_container_width=True)

def display_ppa():
    # if 'pg_num' not in stream.session_state:
    #    stream.session_state.pg_num = 0
    sql = f"""SELECT
    authors.authorname AS AuthorName,
    round(sum(books.price) / count(books)) AS AveragePrice
FROM
    books,
    authors
WHERE
    books.authorid = authors.authorid
GROUP BY
    authors.authorid"""
    stream.code(f"Executed Query: \n{sql}", language='sql')
    cursor.execute(sql)
    column_names = [col[0] for col in cursor.description]
    final_result = pd.DataFrame(cursor.fetchall(), columns=column_names)
    stream.dataframe(final_result, use_container_width=True)

# def reset_page_function():
#    stream.session_state.pg_num = 0