from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import WarehouseInterface
from .model import Warehouse
from .schema import WarehouseSchema
from .service import WarehousesService

api = Namespace("Warehouse", description="Single namespace, single entity")

service = WarehousesService


@api.route("/")
class WarehouseResource(Resource):

    @responds(schema=WarehouseSchema(many=True))
    def get(self) -> List[Warehouse]:
        return service.get_all(self)

    @accepts(schema=WarehouseSchema, api=api)
    @responds(schema=WarehouseSchema)
    def post(self) -> Warehouse:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:WarehouseId>")
@api.param("WarehousesId", "Warehouse database ID")
class WarehouseIdResource(Resource):
    @responds(schema=WarehouseSchema)
    def get(self, WarehouseId: int) -> Warehouse:
        return service.get_by_id(self, WarehouseId)

    def delete(self, WarehouseId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, WarehouseId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=WarehouseSchema, api=api)
    @responds(schema=WarehouseSchema)
    def put(self, WarehouseId: int) -> Warehouse:
        changes: WarehouseInterface = request.parsed_obj
        warehouse = service.get_by_id(self, WarehouseId)
        return service.update(self, warehouse, changes)
