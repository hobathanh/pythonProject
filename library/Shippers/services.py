from library.extension import db
from library.library_ma import ShipperSchema
from library.model import *
from flask import request, jsonify
from sqlalchemy.sql import func
import json

shipper_schema = ShipperSchema()
shippers_schema = ShipperSchema(many=True)


def add_shipper_service():
    data = request.json
    if (data and ('ShipperName' in data) and ('Phone' in data)):
        ShipperName = data['ShipperName']
        Phone = data['Phone']

        try:
            new_shipper = Shippers(ShipperName, Phone)
            db.session.add(new_shipper)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add shipper!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_shipper_by_id_service(id):
    shipper = Shippers.query.get(id)
    if shipper:
        return shipper_schema.jsonify(shipper)
    else:
        return jsonify({"message": "Not found shipper"}), 404


def get_all_shippers_service():
    shippers = Shippers.query.all()
    if shippers:
        return shippers_schema.jsonify(shippers)
    else:
        return jsonify({"message": "Not found shippers!"}), 404

#update shipper name
def update_shipper_by_id_service(id):
    shipper = Shippers.query.get(id)
    data = request.json
    if shipper:
        if data and "ShipperName" in data:
            try:
                shipper.ShipperName = data["ShipperName"]
                db.session.commit()
                return "Shipper Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update shipper!"}), 400
    else:
        return "Not found shipper"


def delete_shipper_by_id_service(id):
    shipper = Shippers.query.get(id)
    if shipper:
        try:
            db.session.delete(shipper)
            db.session.commit()
            return "Shipper Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete shipper!"}), 400
    else:
        return "Not found shipper"

