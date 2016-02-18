import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from flask import Flask, jsonify

app = Flask(__name__, template_folder="../", static_folder = "../build")

from app.category.urls import category
from app.product.urls import product
from app.search.urls import search
from app.home.urls import home

app.register_blueprint(category, url_prefix='/category')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(home, url_prefix="/")


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Message": "URL not supported"}), 404
