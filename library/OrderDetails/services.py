from library.extension import db
from library.library_ma import OrderDetailSchema
from library.model import *
from flask import request, jsonify
from sqlalchemy.sql import func
import json

order_detail_schema = OrderDetailSchema()
order_details_schema = OrderDetailSchema(many=True)


def add_order_detail_service():
    data = request.json
    if (data and ('OrderID' in data) and ('ProductID' in data)
             and ('Quantity' in data) ):
        OrderID = data['OrderID']
        ProductID = data['ProductID']
        Quantity = data['Quantity']
        
        try:
            new_order_detail = OrderDetails(OrderID, ProductID, Quantity)
            db.session.add(new_order_detail)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add order_detail!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_order_detail_by_id_service(id):
    order_detail = OrderDetails.query.get(id)
    if order_detail:
        return order_detail_schema.jsonify(order_detail)
    else:
        return jsonify({"message": "Not found order_detail"}), 404


def get_all_order_details_service():
    order_details = OrderDetails.query.all()
    if order_details:
        return order_details_schema.jsonify(order_details)
    else:
        return jsonify({"message": "Not found order_detail!"}), 404


# update Quantity
def update_order_detail_by_id_service(id):
    order_detail = OrderDetails.query.get(id)
    data = request.json
    if order_detail:
        if data and "Quantity" in data:
            try:
                order_detail.Quantity = data["Quantity"]
                db.session.commit()
                return "order_detail Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update order!"}), 400
    else:
        return "Not found order_detail"


def delete_order_detail_by_id_service(id):
    order_detail = OrderDetails.query.get(id)
    if order_detail:
        try:
            db.session.delete(order_detail)
            db.session.commit()
            return "order_detail Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete order_detail!"}), 400
    else:
        return "Not found order_detail"

