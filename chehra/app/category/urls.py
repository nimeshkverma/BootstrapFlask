from flask import Blueprint
from views import *

category = Blueprint('category', __name__)

category.add_url_rule(
    '/get_category/<category_id>', view_func=get_category, methods=['GET'])
category.add_url_rule(
    '/post_category<category_id>', view_func=post_category, methods=['POST'])
