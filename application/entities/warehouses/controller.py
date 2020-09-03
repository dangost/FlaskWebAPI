from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import WarehouseSchema
from .service import WarehousesService
from .model import Warehouse
from .interface import WarehouseInterface

api = Namespace("Warehouse", description="Single namespace, single entity")


@api.route("/")
class WarehouseResource(Resource):

    @responds(schema=WarehouseSchema(many=True))
    def get(self) -> List[Warehouse]:

        return WarehousesService.get_all()

    @accepts(schema=WarehouseSchema, api=api)
    @responds(schema=WarehouseSchema)
    def post(self) -> Warehouse:
        obj: dict = request.parsed_obj
        return WarehouseService.create(obj)


@api.route("/<int:WarehouseId>")
@api.param("WarehousesId", "Warehouse database ID")
class WarehouseIdResource(Resource):
    @responds(schema=WarehouseSchema)
    def get(self, WarehouseId: int) -> WarehouseId:
        return WarehousesService.get_by_id(Warehouses)

    def delete(self, WarehouseId: int) -> Response:
        from flask import jsonify

        id: int = WarehousesService.delete_by_id(WarehouseId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=WarehouseSchema, api=api)
    @responds(schema=WarehouseSchema)
    def put(self, WarehouseId: int) -> Warehouse:

        changes: WarehouseInterface = request.parsed_obj
        warehouse = WarehousesService.get_by_id(Warehouses)
        return WarehousesService.update(warehouse, changes)

