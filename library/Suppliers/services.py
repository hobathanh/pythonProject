from library.extension import db
from library.library_ma import SupplierSchema
from library.model import *
from flask import request, jsonify
from sqlalchemy.sql import func
import json

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)


def add_supplier_service():
    data = request.json
    if (data and ('SupplierName' in data) and ('ContactName' in data)
             and ('Address' in data) and ('City' in data) 
             and ('PostalCode' in data) and ('Country' in data)
             and ('Phone' in data)):
        SupplierName = data['SupplierName']
        ContactName = data['ContactName']
        Address = data['Address']
        City = data['City']
        PostalCode = data['PostalCode']
        Country = data['Country']
        Phone = data['Phone']

        try:
            new_supplier = Suppliers(SupplierName, ContactName, Address, City,PostalCode,Country ,Phone)
            db.session.add(new_supplier)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add supplier!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_supplier_by_id_service(id):
    supplier = Suppliers.query.get(id)
    if supplier:
        return supplier_schema.jsonify(supplier)
    else:
        return jsonify({"message": "Not found supplier"}), 404


def get_all_suppliers_service():
    suppliers = Suppliers.query.all()
    if suppliers:
        return suppliers_schema.jsonify(suppliers)
    else:
        return jsonify({"message": "Not found suppliers!"}), 404

#update supplier name
def update_supplier_by_id_service(id):
    supplier = Suppliers.query.get(id)
    data = request.json
    if supplier:
        if data and "SupplierName" in data:
            try:
                supplier.SupplierName = data["SupplierName"]
                db.session.commit()
                return "Supplier Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update supplier!"}), 400
    else:
        return "Not found supplier"


def delete_supplier_by_id_service(id):
    supplier = Suppliers.query.get(id)
    if supplier:
        try:
            db.session.delete(supplier)
            db.session.commit()
            return "Supplier Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete supplier!"}), 400
    else:
        return "Not found supplier"
