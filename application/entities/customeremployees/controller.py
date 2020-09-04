from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CustomerEmployeeSchema
from .service import CustomerEmployeesService
from .model import CustomerEmployee
from .interface import CustomerEmployeeInterface

api = Namespace("CustomerEmployee", description="Single namespace, single entity")


@api.route("/")
class CustomerEmployeeResource(Resource):

    @responds(schema=CustomerEmployeeSchema(many=True))
    def get(self) -> List[CustomerEmployee]:

        return CustomerEmployeesService.get_all()

    @accepts(schema=CustomerEmployeeSchema, api=api)
    @responds(schema=CustomerEmployeeSchema)
    def post(self) -> CustomerEmployee:
        obj: dict = request.parsed_obj
        return CustomerEmployeeService.create(obj)


@api.route("/<int:CustomerEmployeeId>")
@api.param("CustomerEmployeesId", "CustomerEmployee database ID")
class CustomerEmployeeIdResource(Resource):
    @responds(schema=CustomerEmployeeSchema)
    def get(self, CustomerEmployeeId: int) -> CustomerEmployee:
        return CustomerEmployeesService.get_by_id(CustomerEmployeeId)

    def delete(self, CustomerEmployeeId: int) -> Response:
        from flask import jsonify

        id: int = CustomerEmployeesService.delete_by_id(CustomerEmployeeId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CustomerEmployeeSchema, api=api)
    @responds(schema=CustomerEmployeeSchema)
    def put(self, CustomerEmployeeId: int) -> CustomerEmployee:

        changes: CustomerEmployeeInterface = request.parsed_obj
        customeremployee = CustomerEmployeesService.get_by_id(CustomerEmployees)
        return CustomerEmployeesService.update(customeremployee, changes)

