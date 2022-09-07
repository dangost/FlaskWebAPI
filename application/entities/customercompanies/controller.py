from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import CustomerCompanyInterface
from .model import CustomerCompany
from .schema import CustomerCompanySchema
from .service import CustomerCompaniesService

api = Namespace("CustomerCompany", description="Single namespace, single entity")

service = CustomerCompaniesService


@api.route("/")
class CustomerCompanyResource(Resource):

    @responds(schema=CustomerCompanySchema(many=True))
    def get(self) -> List[CustomerCompany]:
        return service.get_all(self)

    @accepts(schema=CustomerCompanySchema, api=api)
    @responds(schema=CustomerCompanySchema)
    def post(self) -> CustomerCompany:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:CompanyId>")
@api.param("CustomerCompaniesId", "CustomerCompany database ID")
class CustomerCompanyIdResource(Resource):
    @responds(schema=CustomerCompanySchema)
    def get(self, CompanyId: int) -> CustomerCompany:
        return service.get_by_id(self, CompanyId)

    def delete(self, CompanyId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, CompanyId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CustomerCompanySchema, api=api)
    @responds(schema=CustomerCompanySchema)
    def put(self, CompanyId: int) -> CustomerCompany:
        changes: CustomerCompanyInterface = request.parsed_obj
        customercompany = service.get_by_id(self, CompanyId)
        return service.update(self, customercompany, changes)
