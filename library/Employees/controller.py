from flask import Blueprint
from .services import (add_employee_service,get_employee_by_id_service,get_all_employees_service,
                        update_employee_by_id_service,delete_employee_by_id_service)
employees = Blueprint("employees", __name__)



# add a new employee
@employees.route("/employee-management/employee", methods = ['POST'])
def add_employee():
    return add_employee_service()
    
# get employee by id
@employees.route("/employee-management/employee/<int:id>", methods = ['GET'])
def get_employee_by_id(id):
    return get_employee_by_id_service(id)

# get all employee
@employees.route("/employee-management/employees", methods=['GET'])
def get_all_employees():
    return get_all_employees_service()


# update employee
@employees.route("/employee-management/employee/<int:id>", methods=['PUT'])
def update_employee_by_id(id):
    return update_employee_by_id_service(id)


# delete employee
@employees.route("/employee-management/employee/<int:id>", methods=['DELETE'])
def delete_employee_by_id(id):
    return delete_employee_by_id_service(id)


