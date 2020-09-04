from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import OrdersSchema
from .service import OrdersService
from .model import Orders
from .interface import OrdersInterface

api = Namespace("Orders", description="Single namespace, single entity")


@api.route("/")
class OrdersResource(Resource):

    @responds(schema=OrdersSchema(many=True))
    def get(self) -> List[Orders]:

        return OrdersService.get_all()

    @accepts(schema=OrdersSchema, api=api)
    @responds(schema=OrdersSchema)
    def post(self) -> Orders:
        obj: dict = request.parsed_obj
        return OrdersService.create(obj)


@api.route("/<int:OrderId>")
@api.param("OrdersId", "Orders database ID")
class OrdersIdResource(Resource):
    @responds(schema=OrdersSchema)
    def get(self, OrderId: int) -> Orders:
        return OrdersService.get_by_id(OrderId)

    def delete(self, OrderId: int) -> Response:
        from flask import jsonify

        id: int = OrdersService.delete_by_id(OrderId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=OrdersSchema, api=api)
    @responds(schema=OrdersSchema)
    def put(self, OrderId: int) -> Orders:

        changes: OrdersInterface = request.parsed_obj
        orders = OrdersService.get_by_id(OrderId)
        return OrdersService.update(orders, changes)

