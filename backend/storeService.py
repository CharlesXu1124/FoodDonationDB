# dependencies imports
import requests
import json
import numpy as np
import random
import string
import json
from flask import Flask
from flask import request,jsonify
from flask_cors import CORS, cross_origin
import math
import pyodbc
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

app = Flask(__name__)
cors = CORS(app, resources={
                r"/signup": {"origins": "*"},
                r"/login": {"origins": "*"},
                r"/placeOrder": {"origins": "*"},
                r"/placeOrderWithTrigger": {"origins": "*"},
                r"/searchRestaurantByLatLng": {"origins": "*"},
                r"/searchMostPopularRestaurants": {"origins": "*"},
                r"/searchRestaurantByLatLngv2" : {"origins": "*"},
                })
app.config['CORS_HEADERS'] = 'Content-Type'

'''
increment amount of food reserve in each restaurant periodically
'''
@tl.job(interval=timedelta(seconds=900))
def produce_food():
    query = '''
    UPDATE [dbo].[Restaurant]
    SET cuisine_qty = cuisine_qty + 1;
    '''
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
    cursor.execute(query)
    
    conn.commit()
    print("Updating food bank..........")
    print(query)



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


'''
function for handling user login authentication request
'''
@app.route('/login', methods=['GET', 'POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def login():
    user_password = request.json['password']
    email = request.json['email']

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

    print("Executing query..........")

    query_string = "select credential, cust_id, cust_name from [dbo].[Customers] where [dbo].[Customers].cust_email='{0}'".format(email)

    print("executing: %s" % query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()
    if row is not None:
        credential,cus_id,cus_name = str(row[0]),str(row[1]),str(row[2])
    else:
        return jsonify({'success':False})

    if credential == user_password:
        return jsonify({'cus_id':cus_id,'success':True,'cus_name':cus_name})

        # print("Login successful!!!")
        # return "Login successful!!!"
    else:
        return jsonify({'success':False})

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
function for handling order placing request
'''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/placeOrder', methods=[ 'POST'])
def placeOrder():
    order_id = random_string(64)
    order_quantity = request.json["order_quantity"]
    cust_id = request.json["cust_id"]
    rID = request.json["rID"]

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
function for handling order placing request
'''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/placeOrderWithTrigger', methods=[ 'POST'])
def placeOrderWithTrigger():
    order_id = random_string(64)
    order_quantity = request.json["order_quantity"]
    cust_id = request.json["cust_id"]
    rID = request.json["rID"]

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
    
    # update order trigger
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            query = "CREATE TRIGGER order_trigger ON [dbo].[Restaurant] AFTER UPDATE AS BEGIN IF 1 > 0 INSERT INTO [dbo].[Orders]  (order_id, order_quantity, cust_id, rID) VALUES ('%s', %d, '%s','%s') END;" % (order_id, order_quantity, cust_id, rID)
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

    # drop the trigger so it won't interfere with the food resupply
    with pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';\
                PORT=1433;DATABASE=' + database + ';\
                    UID=' + username + ';\
                        PWD=' + password) as conn:
        with conn.cursor() as cursor:
            query = 'DROP TRIGGER IF EXISTS order_trigger;'
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
    query_string = "select rID, rName, rCuisine, rPhone, cuisine_qty, rRating, rLatitude, rLongitude from [dbo].[Restaurant];"
    print("Executing query: %s" % query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()


    while row is not None:
        target_lat = float(row[6])
        target_lon = float(row[7])
        distance = calc_distance(user_lat, user_lon, target_lat, target_lon)

        # add the restaurants within search range to the list
        if distance < radius:

            list_of_restaurants.append({
                'id':row[0],
                'name': row[1],
                'cuisine': row[2],
                'phone': row[3],
                'rating': str(row[5]),
                'quantity': int(row[4]),
                'lng': float(row[7]),
                'lat':float(row[6]),
                'distance': int(distance)
            })
        row = cursor.fetchone()

    # sort the returned restaurants according to their proximity to the user
    list_of_restaurants.sort(key = lambda json: json['distance'], reverse=False)

    return (jsonify(list_of_restaurants))

# '''
# return a list of restaurants sorted by popularity
# '''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/searchMostPopularRestaurants', methods=[ 'POST'])
def searchMostPopularRestaurants():
    user_lat = request.json["latitude"]
    user_lon = request.json["longitude"]
    radius = request.json["radius"]


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
    query_string = "select rID, rName, rCuisine, rPhone, cuisine_qty, rRating, rLatitude, rLongitude from [dbo].[Restaurant];"
    print("Executing query: %s" % query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()


    while row is not None:
        target_lat = float(row[6])
        target_lon = float(row[7])
        distance = calc_distance(user_lat, user_lon, target_lat, target_lon)

        # add the restaurants within search range to the list
        if distance < radius:

            list_of_restaurants.append({
                'id':row[0],
                'name': row[1],
                'cuisine': row[2],
                'phone': row[3],
                'rating': str(row[5]),
                'quantity': int(row[4]),
                'lng': float(row[7]),
                'lat':float(row[6]),
                'distance': int(distance),
                'popularity': float(row[5]) - int(distance) / 5000
            })
        row = cursor.fetchone()

    # sort the returned restaurants according to their proximity to the user
    list_of_restaurants.sort(key = lambda json: json['popularity'], reverse=True)

    return (jsonify(list_of_restaurants))


'''
restaurant search function by user latitude and longitude, and search radius (ver. 2.0)
'''
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
@app.route('/searchRestaurantByLatLngv2', methods=[ 'POST'])
def searchRestaurantByLatLngv2():
    user_lat = request.json["latitude"]
    user_lon = request.json["longitude"]
    radius = request.json["radius"]

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
    query_string = "select rID, rName, rCuisine, rPhone, cuisine_qty, rRating, rLatitude, rLongitude from [dbo].[Restaurant];"
    print("Executing query: %s" % query_string)
    cursor.execute(query_string)
    row = cursor.fetchone()


    while row is not None:
        target_lat = float(row[6])
        target_lon = float(row[7])
        distance = calc_distance(user_lat, user_lon, target_lat, target_lon)

        # add the restaurants within search range to the list
        if distance < radius:

            list_of_restaurants.append({
                'id':row[0],
                'name': row[1],
                'cuisine': row[2],
                'phone': row[3],
                'rating': str(row[5]),
                'quantity': int(row[4]),
                'lng': float(row[7]),
                'lat':float(row[6]),
                'distance': int(distance)
            })
        row = cursor.fetchone()

    # sort the returned restaurants according to their proximity to the user
    list_of_restaurants.sort(key = lambda json: json['distance'], reverse=False)

    return (jsonify({"success": True, "results": list_of_restaurants}))



if __name__ == "__main__":
    tl.start(block=False)
    app.run(host='0.0.0.0', port=5000, threaded=True)
