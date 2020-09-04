from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import EmploymentSchema
from .service import EmploymentsService
from .model import Employment
from .interface import EmploymentInterface

api = Namespace("Employment", description="Single namespace, single entity")


@api.route("/")
class EmploymentResource(Resource):

    @responds(schema=EmploymentSchema(many=True))
    def get(self) -> List[Employment]:

        return EmploymentsService.get_all()

    @accepts(schema=EmploymentSchema, api=api)
    @responds(schema=EmploymentSchema)
    def post(self) -> Employment:
        obj: dict = request.parsed_obj
        return EmploymentService.create(obj)


@api.route("/<int:EmployeeID>")
@api.param("EmploymentsId", "Employment database ID")
class EmploymentIdResource(Resource):
    @responds(schema=EmploymentSchema)
    def get(self, EmployeeID: int) -> Employment:
        return EmploymentsService.get_by_id(EmployeeID)

    def delete(self, EmployeeID: int) -> Response:
        from flask import jsonify

        id: int = EmploymentsService.delete_by_id(EmployeeID)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=EmploymentSchema, api=api)
    @responds(schema=EmploymentSchema)
    def put(self, EmployeeID: int) -> Employment:

        changes: EmploymentInterface = request.parsed_obj
        employment = EmploymentsService.get_by_id(Employments)
        return EmploymentsService.update(employment, changes)

