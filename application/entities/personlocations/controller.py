from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import PersonLocationSchema
from .service import PersonLocationsService
from .model import PersonLocation
from .interface import PersonLocationInterface

api = Namespace("PersonLocation", description="Single namespace, single entity")


@api.route("/")
class PersonLocationResource(Resource):

    @responds(schema=PersonLocationSchema(many=True))
    def get(self) -> List[PersonLocation]:

        return PersonLocationsService.get_all()

    @accepts(schema=PersonLocationSchema, api=api)
    @responds(schema=PersonLocationSchema)
    def post(self) -> PersonLocation:
        obj: dict = request.parsed_obj
        return PersonLocationService.create(obj)


@api.route("/<int:>")
@api.param("PersonLocationsId", "PersonLocation database ID")
class PersonLocationIdResource(Resource):
    @responds(schema=PersonLocationSchema)
    def get(self, : int) -> PersonLocation:
        return PersonLocationsService.get_by_id()

    def delete(self, : int) -> Response:
        from flask import jsonify

        id: int = PersonLocationsService.delete_by_id()
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PersonLocationSchema, api=api)
    @responds(schema=PersonLocationSchema)
    def put(self, : int) -> PersonLocation:

        changes: PersonLocationInterface = request.parsed_obj
        personlocation = PersonLocationsService.get_by_id(PersonLocations)
        return PersonLocationsService.update(personlocation, changes)

