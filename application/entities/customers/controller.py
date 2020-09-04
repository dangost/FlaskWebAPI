from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CustomerSchema
from .service import CustomersService
from .model import Customer
from .interface import CustomerInterface

api = Namespace("Customer", description="Single namespace, single entity")

service = CustomersService

@api.route("/")
class CustomerResource(Resource):

    @responds(schema=CustomerSchema(many=True))
    def get(self) -> List[Customer]:
        
        return service.get_all(self)

    @accepts(schema=CustomerSchema, api=api)
    @responds(schema=CustomerSchema)
    def post(self) -> Customer:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:CustomerId>")
@api.param("CustomersId", "Customer database ID")
class CustomerIdResource(Resource):
    @responds(schema=CustomerSchema)
    def get(self, CustomerId: int) -> Customer:
        return service.get_by_id(self, CustomerId)

    def delete(self, CustomerId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, CustomerId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CustomerSchema, api=api)
    @responds(schema=CustomerSchema)
    def put(self, CustomerId: int) -> Customer:

        changes: CustomerInterface = request.parsed_obj
        customer = service.get_by_id(self, CustomerId)
        return service.update(self, customer, changes)

