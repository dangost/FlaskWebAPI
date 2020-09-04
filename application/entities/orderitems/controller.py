from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import OrderItemSchema
from .service import OrderItemsService
from .model import OrderItem
from .interface import OrderItemInterface

api = Namespace("OrderItem", description="Single namespace, single entity")


@api.route("/")
class OrderItemResource(Resource):

    @responds(schema=OrderItemSchema(many=True))
    def get(self) -> List[OrderItem]:

        return OrderItemsService.get_all()

    @accepts(schema=OrderItemSchema, api=api)
    @responds(schema=OrderItemSchema)
    def post(self) -> OrderItem:
        obj: dict = request.parsed_obj
        return OrderItemService.create(obj)


@api.route("/<int:OrderItemId>")
@api.param("OrderItemsId", "OrderItem database ID")
class OrderItemIdResource(Resource):
    @responds(schema=OrderItemSchema)
    def get(self, OrderItemId: int) -> OrderItem:
        return OrderItemsService.get_by_id(OrderItemId)

    def delete(self, OrderItemId: int) -> Response:
        from flask import jsonify

        id: int = OrderItemsService.delete_by_id(OrderItemId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=OrderItemSchema, api=api)
    @responds(schema=OrderItemSchema)
    def put(self, OrderItemId: int) -> OrderItem:

        changes: OrderItemInterface = request.parsed_obj
        orderitem = OrderItemsService.get_by_id(OrderItems)
        return OrderItemsService.update(orderitem, changes)

