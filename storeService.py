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

