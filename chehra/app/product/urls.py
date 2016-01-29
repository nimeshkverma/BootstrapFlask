from flask import Blueprint
from views import *

product = Blueprint('product', __name__)


product.add_url_rule(
    '/get_product/<product_id>', view_func=get_product, methods=['GET'])
product.add_url_rule(
    '/post_product/<product_id>', view_func=post_product, methods=['POST'])
