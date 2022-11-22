from flask import Blueprint
from .services import (add_order_detail_service,get_order_detail_by_id_service,get_all_order_details_service,
                        update_order_detail_by_id_service,delete_order_detail_by_id_service)
order_details = Blueprint("order_details", __name__)



# add a new order_detail
@order_details.route("/order_detail-management/order_detail", methods = ['POST'])
def add_order_detail():
    return add_order_detail_service()
    
# get order_detail by id
@order_details.route("/order_detail-management/order_detail/<int:id>", methods = ['GET'])
def get_order_detail_by_id(id):
    return get_order_detail_by_id_service(id)

# get all order_detail
@order_details.route("/order_detail-management/order_details", methods=['GET'])
def get_all_order_details():
    return get_all_order_details_service()


# update order_detail
@order_details.route("/order_detail-management/order_detail/<int:id>", methods=['PUT'])
def update_order_detail_by_id(id):
    return update_order_detail_by_id_service(id)


# delete order_detail
@order_details.route("/order_detail-management/order_detail/<int:id>", methods=['DELETE'])
def delete_order_detail_by_id(id):
    return delete_order_detail_by_id_service(id)


