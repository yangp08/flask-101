# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! Bonjour"

@app.route('/api/v1/products')
def get_product():
    PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    }


    #return jsonify(firstname='toto',lastname='titi')
    return PRODUCTS
