# dependencies imports
import requests
import json
import numpy as np
import random
import string
import datetime
import json
from flask import Flask
from flask import request,jsonify
from flask_cors import CORS, cross_origin
import pyodbc

# drivers = [item for item in pyodbc.drivers()]
# driver = drivers[-1]
# server = 'ubuntu1.database.windows.net'
# database = 'DB1'
# username = 'admin1'
# password = 'Pwned_2023'
# driver = '{ODBC Driver 17 for SQL Server}'
# conn = pyodbc.connect(
#     'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# cursor = conn.cursor()

app = Flask(__name__)
cors = CORS(app, resources={
                r"/signup": {"origins": "*"},
                r"/login": {"origins": "*"},
                r"/placeOrder": {"origins": "*"},
                r"/searchRestaurantByLatLng": {"origins": "*"},
                })
app.config['CORS_HEADERS'] = 'Content-Type'


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
'''
helper function for calculating the distance between two geocoordinates
'''
def calc_distance(user_lat, user_lon, target_lat, target_lon):
    r = 6371e3
    user_lat_radian = user_lat * math.pi / 180
    target_lat_radian = target_lat * math.pi / 180
    d_lat = (target_lat - user_lat) * math.pi / 180
    d_lon = (target_lon - user_lon) * math.pi / 180

    a = (math.sin(d_lat / 2))**2 + math.cos(user_lat_radian) * math.cos(target_lat_radian) * math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r * c

@app.route('/')
def index():
    return 'invalid call'

@app.route('/login', methods=['GET', 'POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def login():

    password = request.json['password']
    email = request.json['email']

    print("Executing query..........",password,email)

    query_string = "select credential,cust_id,cus_name from [dbo].[Customers] where [dbo].[Customers].cust_email='{0}'".format(email)
    cursor.execute(query_string)
    row = cursor.fetchone()

    credential,cus_id,cus_name = str(row[0]),str(row[1]),str(row[2])

    if credential == password:
        return jsonify({'cus_id':cus_id,'success':True,'cus_name':cus_name})

        # print("Login successful!!!")
        # return "Login successful!!!"
    else:
        return jsonify({'success':False})

        # return "Login failed, check username and password"




'''
function for handling user signup request
'''
@app.route('/signup', methods=['GET', 'POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def signup():
    # randomly generate customer ID during signup
    cust_id = random_string_lower_case(64)

    cust_name = request.json["cust_name"]
    cust_email = request.json["cust_email"]
    cust_phone = request.json["cust_phone"]
    credential = request.json["credential"]



    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]
    print("driver:{}".format(driver))

    server = 'ubuntu1.database.windows.net'
    database = 'DB1'
    username = 'admin1'
    password = 'Pwned_2023'
    driver = '{ODBC Driver 17 for SQL Server}'
    # print(response.json())

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
            
    return jsonify({'cust_id':cust_id,'success':True,'cust_name':cust_name})

'''
function for handling restaurant search request
'''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/searchRestaurant', methods=['GET'])
def searchRestaurant():
    zipcode = request.json['zipcode']

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
    for _, tuple in enumerate(list_of_restaurants):
        results['rName'] = tuple[0]
        results['Cuisine'] = tuple[1]
        results['phone'] = tuple[2]
        results['Address'] = tuple[3]
        results['rating'] = str(tuple[4])
        final_results.append(results)

    return (jsonify(final_results))

@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/placeOrder', methods=[ 'POST'])
def placeOrder():
    order_id = random_string(64)
    order_quantity = request.json["order_quantity"]
    cust_id = request.json["cust_id"]
    rID = request.json["rID"]

    print("Placing order",order_id,order_quantity,cust_id,rID)


    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]
    print("driver:{}".format(driver))

    server = 'ubuntu1.database.windows.net'
    database = 'DB1'
    username = 'admin1'
    password = 'Pwned_2023'
    driver = '{ODBC Driver 17 for SQL Server}'
    
    if order_quantity < 1:
        return jsonify({'success': False, 'info': 'invalid transaction'})

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
                return jsonify({'success': False, 'info': 'not enough food'})

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

    return jsonify({'success':True})
  
'''
restaurant search function by user latitude and longitude, and search radius
'''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/searchRestaurantByLatLng', methods=[ 'POST'])
def searchRestaurantByLatLng():
    user_lat = request.json["latitude"]
    user_lon = request.json["longitude"]
    radius = request.json["radius"]

    print(user_lat,user_lon,radius)

    drivers = [item for item in pyodbc.drivers()]
    driver = drivers[-1]
    server = 'ubuntu1.database.windows.net'
    database = 'DB1'
    username = 'admin1'
    db_password = 'Pwned_2023'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + db_password)
    cursor = conn.cursor()


    list_of_restaurants = []
    query_string = "select rName, rCuisine, rPhone, rAddress, rRating, rLatitude, rLongitude, cuisine_qty from [dbo].[Restaurant];"
    print("Executing query: %s" % query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()


    while row is not None:
        target_lat = float(row[5])
        target_lon = float(row[6])
        distance = calc_distance(user_lat, user_lon, target_lat, target_lon)

        # add the restaurants within search range to the list
        if distance < radius:
            list_of_restaurants.append({
                'rName': row[0],
                'Cuisine': row[1],
                'phone': row[2],
                'Address': row[3],
                'rating': str(row[4]),
                'latitude': float(row[5]),
                'longitude': float(row[6]),
                'cuisine_qty':int(row[7])
                'distance': distance
            })
        row = cursor.fetchone()

    return (jsonify(list_of_restaurants))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
