import numpy as np
import streamlit as stream
import pandas as panda

from sql_connect import current, connection

# stream.session_state.pg_num = 0
# stream.session_state.submit = False
# stream.session_state.insert = []
# stream.session_state.id = 0
# stream.session_state.name = ''

def run():
    column_dict = {}
    stream.session_state.title = ""
    stream.session_state.title = stream.text_input('Query', '')
    @stream.experimental_memo(ttl=600)
    def run_query(query):
        print("runquery called", query)
        query = query + ";"
        with connection.cursor() as current:
            current.execute(query)
            stream.table(current.fetchall())
    # stream.write(stream.session_state.title)


    # Print results.
    # print("out",stream.session_state.title)
    # if stream.session_state.title:
    if stream.button("Execute Query"):
        # stream.write('Why hello there')
        run_query(stream.session_state.title)
        # print("inside button", stream.session_state.title)
        # rows = run_query(stream.session_state.title)
        # for row in rows:
        #     stream.write(f"{row[0]} has a :{row[1]}:")
        # print(stream.session_state.title)
        # stream.session_state.title = ""
    # else:
    #     stream.write("Goodbye")
    # else:
    #     stream.button('Execute Query')


