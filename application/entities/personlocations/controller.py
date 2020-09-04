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

service = PersonLocationsService

@api.route("/")
class PersonLocationResource(Resource):

    @responds(schema=PersonLocationSchema(many=True))
    def get(self) -> List[PersonLocation]:
        
        return service.get_all(self)

    @accepts(schema=PersonLocationSchema, api=api)
    @responds(schema=PersonLocationSchema)
    def post(self) -> PersonLocation:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:PeoplePersonId>")
@api.param("PersonLocationsId", "PersonLocation database ID")
class PersonLocationIdResource(Resource):
    @responds(schema=PersonLocationSchema)
    def get(self, PeoplePersonId: int) -> PersonLocation:
        return service.get_by_id(self, PeoplePersonId)

    def delete(self, PeoplePersonId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, PeoplePersonId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PersonLocationSchema, api=api)
    @responds(schema=PersonLocationSchema)
    def put(self, PeoplePersonId: int) -> PersonLocation:

        changes: PersonLocationInterface = request.parsed_obj
        personlocation = service.get_by_id(self, PeoplePersonId)
        return service.update(self, personlocation, changes)

