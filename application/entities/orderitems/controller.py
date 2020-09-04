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

service = OrderItemsService

@api.route("/")
class OrderItemResource(Resource):

    @responds(schema=OrderItemSchema(many=True))
    def get(self) -> List[OrderItem]:
        
        return service.get_all(self)

    @accepts(schema=OrderItemSchema, api=api)
    @responds(schema=OrderItemSchema)
    def post(self) -> OrderItem:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:OrderItemId>")
@api.param("OrderItemsId", "OrderItem database ID")
class OrderItemIdResource(Resource):
    @responds(schema=OrderItemSchema)
    def get(self, OrderItemId: int) -> OrderItem:
        return service.get_by_id(self, OrderItemId)

    def delete(self, OrderItemId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, OrderItemId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=OrderItemSchema, api=api)
    @responds(schema=OrderItemSchema)
    def put(self, OrderItemId: int) -> OrderItem:

        changes: OrderItemInterface = request.parsed_obj
        orderitem = service.get_by_id(self, OrderItemId)
        return service.update(self, orderitem, changes)

