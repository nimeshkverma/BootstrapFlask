from flask import Blueprint
from views import *

home = Blueprint('home', __name__)

home.add_url_rule(
    '/', view_func=get_index, methods=['GET'])

