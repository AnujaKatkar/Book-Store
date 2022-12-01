# Script 5 - Table Orders
# columns - orderID, customerID, orderDate, Total
import csv
import random
import pandas as pd
from datetime import datetime, timedelta

def create():
    data_dir = './Data_Files/'
    # f = open(f'{data_dir}orders.csv', 'w')

    order_details = pd.read_csv(f'{data_dir}orderDetails.csv')

    total = order_details.groupby(['OrderID']).Price.sum()
    total = total.reset_index()

    customer_id = list(range(1, 20001))

    order_date = list()
    cust_id = list()

    min_year = 2020
    max_year = datetime.now().year
    start = datetime(min_year, 1, 1)
    years = max_year - min_year+1
    end = start + timedelta(days=365 * years)

    for _ in range(total.shape[0]):
        cust_id.append(random.choice(customer_id))
        random_date = start + (end - start) * random.random()
        oDate = random_date.date()
        order_date.append(oDate)

    cust_id = pd.Series(cust_id)
    order_date = pd.Series(order_date)


    total = pd.concat([total, cust_id, order_date], axis=1)
    total.columns = ['OrderID', 'total', 'CustomerID', 'OrderDate']
    total = total[['OrderID', 'CustomerID', 'OrderDate', 'total']]
    total.sort_values(by=['OrderID'])

    total.drop('OrderID', axis=1, inplace=True)

    total.to_csv(f"{data_dir}/orders.csv", index=False)