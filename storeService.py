# dependencies imports
import requests
import json
import numpy as np
import random
import string
import datetime
import json
from flask import Flask
from flask import request

import pyodbc

drivers = [item for item in pyodbc.drivers()]
driver = drivers[-1]
server = 'ubuntu1.database.windows.net'
database = 'DB1'
username = 'admin1'
password = 'Pwned_2023'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    print("Executing query..........")

    query_string = "select credential from [dbo].[Customers] where [dbo].[Customers].cust_email='{0}'".format(email)
    cursor.execute(query_string)
    row = cursor.fetchone()

    credential = str(row[0])

    if credential == password:

        print("Login successful!!!")
        return "Login successful!!!"
    else:
        return "Login failed, check username and password"


@app.route('/searchRestaurant', methods=['GET', 'POST'])
def searchRestaurant():
    zipcode = request.args.get('zipcode')

    list_of_restaurants = []
    query_string = "select rName, rCuisine, rPhone, rAddress, rRating  from [dbo].[Restaurant] where rAddress LIKE '%" + zipcode + "%'"
    print(query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()

    while row is not None:
        list_of_restaurants.append(row)
        row = cursor.fetchone()
    print(list_of_restaurants)

    results = {}
    final_results = []
    for index, tuple in enumerate(list_of_restaurants):
        results['rName'] = tuple[0]
        results['Cuisine'] = tuple[1]
        results['phone'] = tuple[2]
        results['Address'] = tuple[3]
        results['rating'] = str(tuple[4])
        final_results.append(results)

    return (str(final_results))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)