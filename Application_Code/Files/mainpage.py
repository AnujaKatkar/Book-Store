import numpy as np
import streamlit as stream
import pandas as pd

from sql_connect import cursor, connection

def run():

    
    stream.session_state.title = ""
    
    tables = ['Authors', 'Books', 'Countries', 'Customers', 'Orders', 'Order Details', 'Publications']
    tables.sort()

    table = stream.sidebar.selectbox("Tables", tables)
    table_name = "".join(table.lower().split())

    sql = f"SELECT * FROM {table_name};"

    try:
        cursor.execute(sql)
        column_names = [desc[0] for desc in cursor.description]
        
        df = cursor.fetchall()
        df = pd.DataFrame(df, columns=column_names)

        caption = f"<h3 style='text-align: center'>{table} Table</h3>"
        stream.caption(caption, unsafe_allow_html=True)
        
        stream.dataframe(df, use_container_width=True)

        stream.session_state.title = stream.text_input('Query', stream.session_state.title)

        def run_query(query):
            # print("runquery called", query)
            query = query + ";"
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                data = pd.DataFrame(result, columns=column_names)
                stream.dataframe(data, use_container_width=True)

        def insert_data(query):
            # print("runquery called", query)
            query = query + ";"
            with connection.cursor() as cursor:
                cursor.execute(query)
                table_name = ""
                query_values = query.split()
                # print(query_values)
                if query_values[0][0] == "I" or query_values[0][0] == "i" :
                    # print("inside insert")
                    value = query_values[2]
                    for i in value:
                        if i=="(":
                            break
                        table_name += i
                elif query_values[0][0] == "D" or query_values[0][0] == "d":
                    table_name = query_values[2]
                elif query_values[0][0] == "U" or query_values[0][0] == "u":
                    table_name = query_values[1]
                # print(table_name)
                newquery = 'Select * from ' + table_name + ";"
                run_query(newquery)

        # col1, col2 = stream.columns([1,1])
        # with col1:
        #     if stream.button('Insert/Update/Delete Query'):
        #         insert_data(stream.session_state.title)
        # with col2:
        #     if stream.button('Select Query'):
        #         run_query(stream.session_state.title)

        with stream.form(key = "myform"):
            col1, col2 = stream.columns([0.4,2.5])
            with col1:
                select_button = stream.form_submit_button('Select Query')
            with col2:
                insert_button = stream.form_submit_button('Insert/Update/Delete Query')
        
        if select_button:
            run_query(stream.session_state.title)
        if insert_button:
            insert_data(stream.session_state.title)
    except Exception as e:
        stream.write("Error in Query",e)
    


