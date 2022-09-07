from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import PhoneNumberInterface
from .model import PhoneNumber
from .schema import PhoneNumberSchema
from .service import PhoneNumbersService

api = Namespace("PhoneNumber", description="Single namespace, single entity")

service = PhoneNumbersService


@api.route("/")
class PhoneNumberResource(Resource):

    @responds(schema=PhoneNumberSchema(many=True))
    def get(self) -> List[PhoneNumber]:
        return service.get_all(self)

    @accepts(schema=PhoneNumberSchema, api=api)
    @responds(schema=PhoneNumberSchema)
    def post(self) -> PhoneNumber:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:PhoneNumberId>")
@api.param("PhoneNumbersId", "PhoneNumber database ID")
class PhoneNumberIdResource(Resource):
    @responds(schema=PhoneNumberSchema)
    def get(self, PhoneNumberId: int) -> PhoneNumber:
        return service.get_by_id(self, PhoneNumberId)

    def delete(self, PhoneNumberId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, PhoneNumberId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PhoneNumberSchema, api=api)
    @responds(schema=PhoneNumberSchema)
    def put(self, PhoneNumberId: int) -> PhoneNumber:
        changes: PhoneNumberInterface = request.parsed_obj
        phonenumber = service.get_by_id(self, PhoneNumberId)
        return service.update(self, phonenumber, changes)
