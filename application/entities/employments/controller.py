from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import EmploymentInterface
from .model import Employment
from .schema import EmploymentSchema
from .service import EmploymentsService

api = Namespace("Employment", description="Single namespace, single entity")

service = EmploymentsService


@api.route("/")
class EmploymentResource(Resource):

    @responds(schema=EmploymentSchema(many=True))
    def get(self) -> List[Employment]:
        return service.get_all(self)

    @accepts(schema=EmploymentSchema, api=api)
    @responds(schema=EmploymentSchema)
    def post(self) -> Employment:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:EmployeeID>")
@api.param("EmploymentsId", "Employment database ID")
class EmploymentIdResource(Resource):
    @responds(schema=EmploymentSchema)
    def get(self, EmployeeID: int) -> Employment:
        return service.get_by_id(self, EmployeeID)

    def delete(self, EmployeeID: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, EmployeeID)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=EmploymentSchema, api=api)
    @responds(schema=EmploymentSchema)
    def put(self, EmployeeID: int) -> Employment:
        changes: EmploymentInterface = request.parsed_obj
        employment = service.get_by_id(self, EmployeeID)
        return service.update(self, employment, changes)
