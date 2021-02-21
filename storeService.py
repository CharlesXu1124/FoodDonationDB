# dependencies imports
import requests
import json
import numpy as np
import random
import string
import datetime

from flask import Flask
from flask import request

import pyodbc


app = Flask(__name__)

# helper function for generating random hashes
def random_string(length):
    pool = string.ascii_uppercase + string.digits
    return ''.join(random.choice(pool) for i in range(length))

def random_digits(length):
    pool = string.digits
    return ''.join(random.choice(pool) for i in range(length))

def random_string_lower_case(length):
    pool = string.ascii_lowercase + string.digits
    return ''.join(random.choice(pool) for i in range(length))



@app.route('/')
def index():
    return 'invalid call'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    data = request.data
    loaded_json = json.loads(data)
    cust_id = loaded_json["cust_id"]
    cust_name = loaded_json["cust_name"]
    cust_email = loaded_json["cust_email"]
    cust_phone = loaded_json["cust_phone"]
    credential = loaded_json["credential"]

    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]
    print("driver:{}".format(driver))

    server = 'ubuntu1.database.windows.net'
    database = 'DB1'
    username = 'admin1'
    password = 'Pwned_2023'
    driver = '{ODBC Driver 17 for SQL Server}'
    # print(response.json())

    result_from_database = []
    

    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO [dbo].[Customers] \
                 (cust_id, cust_name, cust_email, cust_phone, credential) \
                     VALUES ('%s', '%s', '%s', '%s', '%s');" % (cust_id, cust_name, cust_email, cust_phone, credential))
            # cursor.execute("SELECT * FROM [dbo].[Customers];")
            conn.commit()
            # row = cursor.fetchone()

            while row is not None:
                result_from_database.append(row)
                row = cursor.fetchone()
            print(result_from_database)
    return "account created successfully"


# @app.route('/login', methods=['GET', 'POST'])
# def login():


# @app.route('/searchRestaurant', methods=['GET', 'POST'])
# def searchRestaurant():


@app.route('/placeOrder', methods=['GET', 'POST'])
def placeOrder():
    data = request.data
    loaded_json = json.loads(data)
    order_id = random_string(64)
    order_quantity = loaded_json["order_quantity"]
    cust_id = loaded_json["cust_id"]
    rID = loaded_json["rID"]

    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]
    print("driver:{}".format(driver))

    server = 'ubuntu1.database.windows.net'
    database = 'DB1'
    username = 'admin1'
    password = 'Pwned_2023'
    driver = '{ODBC Driver 17 for SQL Server}'

    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cuisine_qty FROM [dbo].[Restaurant] WHERE rID = '%s';" % (rID))
            # cursor.execute("SELECT * FROM [dbo].[Customers];")
            
            row = cursor.fetchone()[0]

            if row is not None:
                print(row)

            if row < order_quantity:
                return "Transaction failed: not enough food"
    
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            query = "INSERT INTO Orders \
                (order_id, order_quantity, cust_id, rID) VALUES \
                ('%s', %s, '%s', '%s')" % (order_id, order_quantity, cust_id, rID)
            print("executing query: %s" % query)
            cursor.execute(query)
            # cursor.execute("SELECT * FROM [dbo].[Customers];")
            conn.commit()

    quantity_remaining = row - order_quantity
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            query = "UPDATE [dbo].[Restaurant] \
                SET cuisine_qty = %d FROM [dbo].[Restaurant] WHERE RID = '%s';" % (quantity_remaining, rID)
            print("executing query: %s" % query)
            cursor.execute(query)
            # cursor.execute("SELECT * FROM [dbo].[Customers];")
            conn.commit()
    
    return "Order placed, thank you for choosing us!"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)