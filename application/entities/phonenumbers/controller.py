from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import PhoneNumberSchema
from .service import PhoneNumbersService
from .model import PhoneNumber
from .interface import PhoneNumberInterface

api = Namespace("PhoneNumber", description="Single namespace, single entity")


@api.route("/")
class PhoneNumberResource(Resource):

    @responds(schema=PhoneNumberSchema(many=True))
    def get(self) -> List[PhoneNumber]:

        return PhoneNumbersService.get_all()

    @accepts(schema=PhoneNumberSchema, api=api)
    @responds(schema=PhoneNumberSchema)
    def post(self) -> PhoneNumber:
        obj: dict = request.parsed_obj
        return PhoneNumbersService.create(obj)


@api.route("/<int:PhoneNumberId>")
@api.param("PhoneNumbersId", "PhoneNumber database ID")
class PhoneNumberIdResource(Resource):
    @responds(schema=PhoneNumberSchema)
    def get(self, PhoneNumberId: int) -> PhoneNumber:
        return PhoneNumbersService.get_by_id(PhoneNumberId)

    def delete(self, PhoneNumberId: int) -> Response:
        from flask import jsonify

        id: int = PhoneNumbersService.delete_by_id(PhoneNumberId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PhoneNumberSchema, api=api)
    @responds(schema=PhoneNumberSchema)
    def put(self, PhoneNumberId: int) -> PhoneNumber:

        changes: PhoneNumberInterface = request.parsed_obj
        phonenumber = PhoneNumbersService.get_by_id(PhoneNumberId)
        return PhoneNumbersService.update(phonenumber, changes)

