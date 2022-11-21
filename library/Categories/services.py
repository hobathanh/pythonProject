from library.extension import db
from library.library_ma import CategorySchema
from library.model import Categories
from flask import request, jsonify
# from sqlalchemy.sql import func
# import json

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


def add_category_service():
    data = request.json
    if (data and ('CategoryName' in data) and ('Description' in data)):
        CategoryName = data['CategoryName']
        Description = data['Description']

        try:
            new_category = Categories(CategoryName, Description)
            db.session.add(new_category)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add category!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

# def get_category_by_id_service(id):
#     category = Categories.query.get(id)
#     if category:
#         return category_schema.jsonify(category)
#     else:
#         return jsonify({"message": "Not found category"}), 404


# def get_all_categories_service():
#     categories = Categories.query.all()
#     if categories:
#         return categories_schema.jsonify(categories)
#     else:
#         return jsonify({"message": "Not found categories!"}), 404