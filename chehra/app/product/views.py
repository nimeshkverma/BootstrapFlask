import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *
from utils import *

from flask import jsonify, request, current_app, render_template


def get_product(product_id):
    response = jsonify({'get_product': product_id})
    current_app.logger.critical('get_product')
    return response


def post_product(product_id):
    response = jsonify({'post_product': product_id})
    current_app.logger.critical('post_product')
    return response
