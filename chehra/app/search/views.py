import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *
from utils import *

from flask import jsonify, request, current_app, render_template


def get_search(query):
    response = jsonify({'get_search': query})
    current_app.logger.critical('get_search')
    return response


def post_search(query):
    response = jsonify({'post_search': query})
    current_app.logger.critical('post_search')
    return response
