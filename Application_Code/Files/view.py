import streamlit as stream
import pandas as pd
from sql_connect import cursor, connection

def run():
    tables = ['Authors', 'Books', 'Countries', 'Custreamomers', 'Orders', 'Order Details', 'Publications']
    tables.sort()

    table = stream.sidebar.selectbox("Tables", tables)
    table_name = "".join(table.lower().split())

    sql = f"SELECT * FROM {table_name};"

    cursor.execute(sql)
    column_names = [desc[0] for desc in cursor.description]
    
    df = cursor.fetchall()
    df = pd.DataFrame(df, columns=column_names)

    caption = f"<h3 streamyle='text-align: center'>{table} Table</h3>"
    stream.caption(caption, unsafe_allow_html=True)
    
    stream.dataframe(df, use_container_width=True)

    select_columns = stream.sidebar.multiselect(f"Select Columns from {table} Table", column_names)
    filter_columns = stream.sidebar.multiselect(f"Filter table on columns", column_names)

    mapping = dict()
    for col in filter_columns:
        condition = stream.sidebar.selectbox(f"Choose operator for '{col}'", ['<', '>', '<=', '>=', "=", "<>", "in", "not in", "like", "not like", "between", "not between", "is null", "is not null", "is true", "is not true", "is false", "is not false"])
        value = stream.sidebar.text_input(f"Enter value to filter-on for '{col}'")
        logical_condition = stream.sidebar.selectbox(f"Enter logical operator for '{col}'", ['Blank', 'AND', 'OR'])
        mapping[col] = (condition, value, logical_condition)

    # if stream.button('Run Query'):
    #     run_query(mapping)


    with stream.form(key = 'view_form'):
        submit = stream.form_submit_button('Run Query')
    if submit:
        run_query(mapping, select_columns, filter_columns, table_name)

def run_query(mapping, select_columns, filter_columns, table_name):
    if len(select_columns) == 0:
        sql = f"SELECT * FROM {table_name}"
    else:
        sql = f"SELECT {','.join(select_columns)} FROM {table_name}"
    
    if filter_columns:
        sql += " WHERE"
        for key, values in mapping.items():
            condition, value, logical_condition = values
            if condition in ['between', 'not between']:
                num1, num2 = value.split(',')
                sql += f" {key} {condition} {num1} AND {num2}"
            elif condition in ["is null", "is not null", "is true", "is not true", "is false", "is not false"]:
                sql += f" {key} {condition}"
            elif value.isdigit():
                sql += f" {key} {condition} {value}"
            else:
                sql += f" {key} {condition} '{value}'"
            if logical_condition != 'Blank':
                sql += f" {logical_condition}"
    
    try:
        stream.code(f"Executed Query: \n{sql}", language='sql')
        # stream.write("Executed Query: ",sql)
        cursor.execute(sql)
        column_names = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()
        data = pd.DataFrame(result, columns=column_names)
        stream.write("Query Result:")
        stream.dataframe(data, use_container_width=True)
    except Exception as e:
        stream.write("Please enter a valid SQL query.")