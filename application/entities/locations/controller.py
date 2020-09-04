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


@api.route("/")
class LocationResource(Resource):

    @responds(schema=LocationSchema(many=True))
    def get(self) -> List[Location]:

        return LocationsService.get_all()

    @accepts(schema=LocationSchema, api=api)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        obj: dict = request.parsed_obj
        return LocationService.create(obj)


@api.route("/<int:LocationId>")
@api.param("LocationsId", "Location database ID")
class LocationIdResource(Resource):
    @responds(schema=LocationSchema)
    def get(self, LocationId: int) -> Location:
        return LocationsService.get_by_id(LocationId)

    def delete(self, LocationId: int) -> Response:
        from flask import jsonify

        id: int = LocationsService.delete_by_id(LocationId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=LocationSchema, api=api)
    @responds(schema=LocationSchema)
    def put(self, LocationId: int) -> Location:

        changes: LocationInterface = request.parsed_obj
        location = LocationsService.get_by_id(Locations)
        return LocationsService.update(location, changes)

