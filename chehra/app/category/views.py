import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *
from utils import *

from flask import jsonify, request, current_app, render_template


def get_category(category_id):
    response = jsonify({'get_category': category_id})
    current_app.logger.critical('get_category')
    return render_template('category/category.html', category_id=category_id)


def post_category(category_id):
    response = jsonify({'post_category': category_id})
    current_app.logger.critical('post_category')
    return response
