from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import RestrictedInfoSchema
from .service import RestrictedInfoService
from .model import RestrictedInfo
from .interface import RestrictedInfoInterface

api = Namespace("RestrictedInfo", description="Single namespace, single entity")


@api.route("/")
class RestrictedInfoResource(Resource):

    @responds(schema=RestrictedInfoSchema(many=True))
    def get(self) -> List[RestrictedInfo]:

        return RestrictedInfoService.get_all()

    @accepts(schema=RestrictedInfoSchema, api=api)
    @responds(schema=RestrictedInfoSchema)
    def post(self) -> RestrictedInfo:
        obj: dict = request.parsed_obj
        return RestrictedInfoService.create(obj)


@api.route("/<int:PersonId>")
@api.param("RestrictedInfoId", "RestrictedInfo database ID")
class RestrictedInfoIdResource(Resource):
    @responds(schema=RestrictedInfoSchema)
    def get(self, PersonId: int) -> RestrictedInfo:
        return RestrictedInfoService.get_by_id(PersonId)

    def delete(self, PersonId: int) -> Response:
        from flask import jsonify

        id: int = RestrictedInfoService.delete_by_id(PersonId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=RestrictedInfoSchema, api=api)
    @responds(schema=RestrictedInfoSchema)
    def put(self, PersonId: int) -> RestrictedInfo:

        changes: RestrictedInfoInterface = request.parsed_obj
        restrictedinfo = RestrictedInfoService.get_by_id(PersonId)
        return RestrictedInfoService.update(restrictedinfo, changes)

