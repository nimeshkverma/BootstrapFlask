import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from flask import Flask, jsonify

app = Flask(__name__)

from app.category.urls import category
from app.product.urls import product
from app.search.urls import search

app.register_blueprint(category, url_prefix='/category')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(search, url_prefix='/search')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "URL not supported"}), 404
