from flask import Blueprint
from .services import add_category_service,get_category_by_id_service,get_all_categories_service,update_category_by_id_service,delete_category_by_id_service

categories = Blueprint("categories", __name__)


# add a new category
@categories.route("/category-management/category", methods = ['POST'])
def add_category():
    return add_category_service()
    
# get category by id
@categories.route("/category-management/category/<int:id>", methods = ['GET'])
def get_category_by_id(id):
    return get_category_by_id_service(id)

# get all category
@categories.route("/category-management/categories", methods=['GET'])
def get_all_categories():
    return get_all_categories_service()

# update category
@categories.route("/category-management/category/<int:id>", methods=['PUT'])
def update_category_by_id(id):
    return update_category_by_id_service(id)


# delete category
@categories.route("/category-management/category/<int:id>", methods=['DELETE'])
def delete_category_by_id(id):
    return delete_category_by_id_service(id)
