from flask import Blueprint
from .services import (add_order_service,get_order_by_id_service,get_all_orders_service,
                        update_order_by_id_service,delete_order_by_id_service)
orders = Blueprint("orders", __name__)



# add a new order
@orders.route("/order-management/order", methods = ['POST'])
def add_order():
    return add_order_service()
    
# get order by id
@orders.route("/order-management/order/<int:id>", methods = ['GET'])
def get_order_by_id(id):
    return get_order_by_id_service(id)

# get all order
@orders.route("/order-management/orders", methods=['GET'])
def get_all_orders():
    return get_all_orders_service()


# update order
@orders.route("/order-management/order/<int:id>", methods=['PUT'])
def update_order_by_id(id):
    return update_order_by_id_service(id)


# delete order
@orders.route("/order-management/order/<int:id>", methods=['DELETE'])
def delete_order_by_id(id):
    return delete_order_by_id_service(id)


