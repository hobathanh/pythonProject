from library.extension import db
from library.library_ma import CustomerSchema
from library.model import Customers
from flask import request, jsonify
from sqlalchemy.sql import func
import json

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


def add_customer_service():
    data = request.json
    if (data and ('CustomersName' in data) and ('ContactName' in data)
             and ('Address' in data) and ('City' in data)
             and ('PostalCode' in data) and ('Country' in data)):
        CustomersName = data['CustomersName']
        ContactName = data['ContactName']
        Address = data['Address']
        City = data['City']
        PostalCode = data['PostalCode']
        Country = data['Country']
        

        try:
            new_customer = Customers(CustomersName, ContactName, Address, City, PostalCode,Country )
            db.session.add(new_customer)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add customer!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_customer_by_id_service(id):
    customer = Customers.query.get(id)
    if customer:
        return customer_schema.jsonify(customer)
    else:
        return jsonify({"message": "Not found customer"}), 404


def get_all_customers_service():
    customers = Customers.query.all()
    if customers:
        return customers_schema.jsonify(customers)
    else:
        return jsonify({"message": "Not found customers!"}), 404

# update CustomersName
def update_customer_by_id_service(id):
    customer = Customers.query.get(id)
    data = request.json
    if customer:
        if data and "CustomersName" in data:
            try:
                customer.v = data["CustomersName"]
                db.session.commit()
                return "Customer Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update customer!"}), 400
    else:
        return "Not found customer"


def delete_customer_by_id_service(id):
    customer = Customers.query.get(id)
    if customer:
        try:
            db.session.delete(customer)
            db.session.commit()
            return "Customer Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete customer!"}), 400
    else:
        return "Not found customer"

