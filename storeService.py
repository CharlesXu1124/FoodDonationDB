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


@app.route('/login', methods=['GET', 'POST'])
def login():


@app.route('/searchRestaurant', methods=['GET', 'POST'])
def searchRestaurant():


@app.route('/placeOrder', methods=['GET', 'POST'])
def placeOrder():
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)