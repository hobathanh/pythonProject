from flask import Blueprint
from .services import (add_shipper_service,get_shipper_by_id_service,get_all_shippers_service,
                        update_shipper_by_id_service,delete_shipper_by_id_service)
shippers = Blueprint("shippers", __name__)



# add a new shipper
@shippers.route("/shipper-management/shipper", methods = ['POST'])
def add_shipper():
    return add_shipper_service()
    
# get shipper by id
@shippers.route("/shipper-management/shipper/<int:id>", methods = ['GET'])
def get_shipper_by_id(id):
    return get_shipper_by_id_service(id)

# get all shipper
@shippers.route("/shipper-management/shippers", methods=['GET'])
def get_all_shippers():
    return get_all_shippers_service()


# update shipper
@shippers.route("/shipper-management/shipper/<int:id>", methods=['PUT'])
def update_shipper_by_id(id):
    return update_shipper_by_id_service(id)


# delete shipper
@shippers.route("/shipper-management/shipper/<int:id>", methods=['DELETE'])
def delete_shipper_by_id(id):
    return delete_shipper_by_id_service(id)
