from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import InventorySchema
from .service import InventoriesService
from .model import Inventory
from .interface import InventoryInterface

api = Namespace("Inventory", description="Single namespace, single entity")


@api.route("/")
class InventoryResource(Resource):

    @responds(schema=InventorySchema(many=True))
    def get(self) -> List[Inventory]:

        return InventoriesService.get_all()

    @accepts(schema=InventorySchema, api=api)
    @responds(schema=InventorySchema)
    def post(self) -> Inventory:
        obj: dict = request.parsed_obj
        return InventoriesService.create(obj)


@api.route("/<int:InventoryId>")
@api.param("InventoriesId", "Inventory database ID")
class InventoryIdResource(Resource):
    @responds(schema=InventorySchema)
    def get(self, InventoryId: int) -> Inventory:
        return InventoriesService.get_by_id(InventoryId)

    def delete(self, InventoryId: int) -> Response:
        from flask import jsonify

        id: int = InventoriesService.delete_by_id(InventoryId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=InventorySchema, api=api)
    @responds(schema=InventorySchema)
    def put(self, InventoryId: int) -> Inventory:

        changes: InventoryInterface = request.parsed_obj
        inventory = InventoriesService.get_by_id(InventoryId)
        return InventoriesService.update(inventory, changes)

