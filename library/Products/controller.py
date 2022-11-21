from flask import Blueprint
from .services import (add_product_service,get_product_by_id_service,get_all_products_service,
                        update_product_by_id_service,delete_product_by_id_service,get_product_by_category_service)
products = Blueprint("products", __name__)



# add a new product
@products.route("/product-management/product", methods = ['POST'])
def add_product():
    return add_product_service()
    
# get product by id
@products.route("/product-management/product/<int:id>", methods = ['GET'])
def get_product_by_id(id):
    return get_product_by_id_service(id)

# get all product
@products.route("/product-management/products", methods=['GET'])
def get_all_products():
    return get_all_products_service()


# update product
@products.route("/product-management/product/<int:id>", methods=['PUT'])
def update_product_by_id(id):
    return update_product_by_id_service(id)


# delete product
@products.route("/product-management/product/<int:id>", methods=['DELETE'])
def delete_product_by_id(id):
    return delete_product_by_id_service(id)


# get product by category
@products.route("/product-management/product/<string:category>", methods=['GET'])
def get_product_by_category(category):
    return get_product_by_category_service(category)
