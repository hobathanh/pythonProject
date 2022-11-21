from flask import Blueprint
# from .services import (add_product_service, get_product_by_id_service,
#                        get_all_products_service, update_product_by_id_service,
#                        delete_product_by_id_service, get_product_by_author_service)
products = Blueprint("products", __name__)

# add a new product


@products.route("/product-management/product")
def add_product():
    # return add_product_service()
    return "all"

# get product by id
