from flask import Blueprint
from .services import add_category_service,get_category_by_id_service,get_all_categories_service

categories = Blueprint("categories", __name__)


# add a new category
@categories.route("/product-management/category", methods = ['POST'])
def add_category():
    return add_category_service()
    
# # get category by id
# @categories.route("/product-management/category/<int:id>", methods = ['GET'])
# def get_category_by_id(id):
#     return get_category_by_id_service(id)

# # get all category
# @categories.route("/product-management/categories", methods=['GET'])
# def get_all_categories():
#     return get_all_categories_service()
