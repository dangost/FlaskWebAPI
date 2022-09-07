from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import RestrictedInfoInterface
from .model import RestrictedInfo
from .schema import RestrictedInfoSchema
from .service import RestrictedInfoService

api = Namespace("RestrictedInfo", description="Single namespace, single entity")

service = RestrictedInfoService


@api.route("/")
class RestrictedInfoResource(Resource):

    @responds(schema=RestrictedInfoSchema(many=True))
    def get(self) -> List[RestrictedInfo]:
        return service.get_all(self)

    @accepts(schema=RestrictedInfoSchema, api=api)
    @responds(schema=RestrictedInfoSchema)
    def post(self) -> RestrictedInfo:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:PersonId>")
@api.param("RestrictedInfoId", "RestrictedInfo database ID")
class RestrictedInfoIdResource(Resource):
    @responds(schema=RestrictedInfoSchema)
    def get(self, PersonId: int) -> RestrictedInfo:
        return service.get_by_id(self, PersonId)

    def delete(self, PersonId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, PersonId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=RestrictedInfoSchema, api=api)
    @responds(schema=RestrictedInfoSchema)
    def put(self, PersonId: int) -> RestrictedInfo:
        changes: RestrictedInfoInterface = request.parsed_obj
        restrictedinfo = service.get_by_id(self, PersonId)
        return service.update(self, restrictedinfo, changes)
