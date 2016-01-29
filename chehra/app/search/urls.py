from flask import Blueprint
from views import *

search = Blueprint('search', __name__)


search.add_url_rule(
    '/get_search/<query>', view_func=get_search, methods=['GET'])
search.add_url_rule(
    '/post_search/<query>', view_func=post_search, methods=['POST'])
