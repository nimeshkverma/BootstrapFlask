import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from common_utils import *
from flask import jsonify, request, current_app, render_template


def get_index():
    return render_template('index.html')
