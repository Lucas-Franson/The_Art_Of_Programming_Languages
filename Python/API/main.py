from flask import *
import json, time
from flask_mysqldb import MySQL


app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return('Welcome')

if __name__ == '__main__':
    app.run(port=7777)
