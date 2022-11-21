from library.extension import db
from library.library_ma import ProductSchema
from library.model import Products,Categories
from flask import request, jsonify
from sqlalchemy.sql import func
import json

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


def add_product_service():
    data = request.json
    if (data and ('ProductName' in data) and ('SupplierID' in data)
             and ('CategoryID' in data) and ('Unit' in data) 
             and ('Price' in data)):
        ProductName = data['ProductName']
        SupplierID = data['SupplierID']
        CategoryID = data['CategoryID']
        Unit = data['Unit']
        Price = data['Price']

        try:
            new_product = Products(ProductName, SupplierID, CategoryID, Unit,Price)
            db.session.add(new_product)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add product!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_product_by_id_service(id):
    product = Products.query.get(id)
    if product:
        return product_schema.jsonify(product)
    else:
        return jsonify({"message": "Not found product"}), 404


def get_all_products_service():
    products = Products.query.all()
    if products:
        return products_schema.jsonify(products)
    else:
        return jsonify({"message": "Not found products!"}), 404

#update product name
def update_product_by_id_service(id):
    product = Products.query.get(id)
    data = request.json
    if product:
        if data and "ProductName" in data:
            try:
                product.ProductName = data["ProductName"]
                db.session.commit()
                return "Product Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update product!"}), 400
    else:
        return "Not found product"


def delete_product_by_id_service(id):
    product = Products.query.get(id)
    if product:
        try:
            db.session.delete(product)
            db.session.commit()
            return "Product Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete product!"}), 400
    else:
        return "Not found product"


def get_product_by_category_service(category):
    products = Products.query.join(Categories).filter(
        func.lower(Categories.CategoryName) == category.lower()).all()
    if products:
        return products_schema.jsonify(products)
    else:
        return jsonify({"message": f"Not found products by {category}"}), 404