from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import LocationSchema
from .service import LocationsService
from .model import Location
from .interface import LocationInterface

api = Namespace("Location", description="Single namespace, single entity")

service = LocationsService

@api.route("/")
class LocationResource(Resource):

    @responds(schema=LocationSchema(many=True))
    def get(self) -> List[Location]:
        
        return service.get_all(self)

    @accepts(schema=LocationSchema, api=api)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:LocationId>")
@api.param("LocationsId", "Location database ID")
class LocationIdResource(Resource):
    @responds(schema=LocationSchema)
    def get(self, LocationId: int) -> Location:
        return service.get_by_id(self, LocationId)

    def delete(self, LocationId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, LocationId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=LocationSchema, api=api)
    @responds(schema=LocationSchema)
    def put(self, LocationId: int) -> Location:

        changes: LocationInterface = request.parsed_obj
        location = service.get_by_id(self, LocationId)
        return service.update(self, location, changes)

