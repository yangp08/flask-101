# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify, abort, request
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET'])
def read_all_products():
    return jsonify(list(PRODUCTS.values())), 200


@app.route('/api/v1/products/<int:id>', methods=['GET'])
def read_one_product(id):
    product = PRODUCTS.get(id)
    if product is None:
        abort(404)

    return jsonify(product)

