from flask import Blueprint
from .services import (add_supplier_service,get_supplier_by_id_service,get_all_suppliers_service,
                        update_supplier_by_id_service,delete_supplier_by_id_service)
suppliers = Blueprint("suppliers", __name__)



# add a new supplier
@suppliers.route("/supplier-management/supplier", methods = ['POST'])
def add_supplier():
    return add_supplier_service()
    
# get supplier by id
@suppliers.route("/supplier-management/supplier/<int:id>", methods = ['GET'])
def get_supplier_by_id(id):
    return get_supplier_by_id_service(id)

# get all supplier
@suppliers.route("/supplier-management/suppliers", methods=['GET'])
def get_all_suppliers():
    return get_all_suppliers_service()


# update supplier
@suppliers.route("/supplier-management/supplier/<int:id>", methods=['PUT'])
def update_supplier_by_id(id):
    return update_supplier_by_id_service(id)


# delete supplier
@suppliers.route("/supplier-management/supplier/<int:id>", methods=['DELETE'])
def delete_supplier_by_id(id):
    return delete_supplier_by_id_service(id)
