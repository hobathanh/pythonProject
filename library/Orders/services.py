from library.extension import db
from library.library_ma import OrderSchema
from library.model import Orders
from flask import request, jsonify
from sqlalchemy.sql import func
import json

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


def add_order_service():
    data = request.json
    if (data and ('CustomerID' in data) and ('EmployeeID' in data)
             and ('OrderDate' in data) and ('ShipperID' in data)):
        CustomerID = data['CustomerID']
        EmployeeID = data['EmployeeID']
        OrderDate = data['OrderDate']
        ShipperID = data['ShipperID']
        

        try:
            new_order = Orders(CustomerID, EmployeeID, OrderDate, ShipperID)
            db.session.add(new_order)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add order!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_order_by_id_service(id):
    order = Orders.query.get(id)
    if order:
        return order_schema.jsonify(order)
    else:
        return jsonify({"message": "Not found order"}), 404


def get_all_orders_service():
    orders = Orders.query.all()
    if orders:
        return orders_schema.jsonify(orders)
    else:
        return jsonify({"message": "Not found orders!"}), 404


def update_order_by_id_service(id):
    order = Orders.query.get(id)
    data = request.json
    if order:
        if data and "ShipperID" in data:
            try:
                order.ShipperID = data["ShipperID"]
                db.session.commit()
                return "Order Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update order!"}), 400
    else:
        return "Not found order"


def delete_order_by_id_service(id):
    order = Orders.query.get(id)
    if order:
        try:
            db.session.delete(order)
            db.session.commit()
            return "Order Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete order!"}), 400
    else:
        return "Not found order"

