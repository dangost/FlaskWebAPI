from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import OrdersInterface
from .model import Orders
from .schema import OrdersSchema
from .service import OrdersService

api = Namespace("Orders", description="Single namespace, single entity")

service = OrdersService


@api.route("/")
class OrdersResource(Resource):

    @responds(schema=OrdersSchema(many=True))
    def get(self) -> List[Orders]:
        return service.get_all(self)

    @accepts(schema=OrdersSchema, api=api)
    @responds(schema=OrdersSchema)
    def post(self) -> Orders:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:OrderId>")
@api.param("OrdersId", "Orders database ID")
class OrdersIdResource(Resource):
    @responds(schema=OrdersSchema)
    def get(self, OrderId: int) -> Orders:
        return service.get_by_id(self, OrderId)

    def delete(self, OrderId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, OrderId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=OrdersSchema, api=api)
    @responds(schema=OrdersSchema)
    def put(self, OrderId: int) -> Orders:
        changes: OrdersInterface = request.parsed_obj
        orders = service.get_by_id(self, OrderId)
        return service.update(self, orders, changes)
