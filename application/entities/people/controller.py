from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import PersonSchema
from .service import PeopleService
from .model import Person
from .interface import PersonInterface

api = Namespace("Person", description="Single namespace, single entity")


@api.route("/")
class PersonResource(Resource):

    @responds(schema=PersonSchema(many=True))
    def get(self) -> List[Person]:

        return PeopleService.get_all()

    @accepts(schema=PersonSchema, api=api)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        obj: dict = request.parsed_obj
        return PeopleService.create(obj)


@api.route("/<int:Id>")
@api.param("PeopleId", "Person database ID")
class PersonIdResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, Id: int) -> Person:
        return PeopleService.get_by_id(Id)

    def delete(self, Id: int) -> Response:
        from flask import jsonify

        id: int = PeopleService.delete_by_id(Id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PersonSchema, api=api)
    @responds(schema=PersonSchema)
    def put(self, Id: int) -> Person:

        changes: PersonInterface = request.parsed_obj
        person = PeopleService.get_by_id(Id)
        return PeopleService.update(person, changes)

