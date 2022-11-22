from library.extension import db
from library.library_ma import EmployeeSchema
from library.model import Employees
from flask import request, jsonify
from sqlalchemy.sql import func
import json

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


def add_employee_service():
    data = request.json
    if (data and ('LastName' in data) and ('FirstName' in data)
             and ('BirthDate' in data) and ('Photo' in data)
             and ('Notes' in data)):
        LastName = data['LastName']
        FirstName = data['BirthDate']
        Photo = data['Photo']
        Notes = data['Notes']
        

        try:
            new_employee = Employees(LastName, FirstName, Photo, Notes)
            db.session.add(new_employee)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add employee!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400

def get_employee_by_id_service(id):
    employee = Employees.query.get(id)
    if employee:
        return employee_schema.jsonify(employee)
    else:
        return jsonify({"message": "Not found employee"}), 404


def get_all_employees_service():
    employees = Employees.query.all()
    if employees:
        return employees_schema.jsonify(employees)
    else:
        return jsonify({"message": "Not found employees!"}), 404


# update Notes
def update_employee_by_id_service(id):
    employee = Employees.query.get(id)
    data = request.json
    if employee:
        if data and "Notes" in data:
            try:
                employee.Notes = data["Notes"]
                db.session.commit()
                return "Employee Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update employee!"}), 400
    else:
        return "Not found employee"


def delete_employee_by_id_service(id):
    employee = Employees.query.get(id)
    if employee:
        try:
            db.session.delete(employee)
            db.session.commit()
            return "Employee Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete employee!"}), 400
    else:
        return "Not found employee"

