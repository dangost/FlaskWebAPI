from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import PersonInterface
from .model import Person
from .schema import PersonSchema
from .service import PeopleService

api = Namespace("Person", description="Single namespace, single entity")

service = PeopleService


@api.route("/")
class PersonResource(Resource):

    @responds(schema=PersonSchema(many=True))
    def get(self) -> List[Person]:
        return service.get_all(self)

    @accepts(schema=PersonSchema, api=api)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:Id>")
@api.param("PeopleId", "Person database ID")
class PersonIdResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, Id: int) -> Person:
        return service.get_by_id(self, Id)

    def delete(self, Id: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, Id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PersonSchema, api=api)
    @responds(schema=PersonSchema)
    def put(self, Id: int) -> Person:
        changes: PersonInterface = request.parsed_obj
        person = service.get_by_id(self, Id)
        return service.update(self, person, changes)
