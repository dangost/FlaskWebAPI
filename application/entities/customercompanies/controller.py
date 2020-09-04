from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CustomerCompanySchema
from .service import CustomerCompaniesService
from .model import CustomerCompany
from .interface import CustomerCompanyInterface

api = Namespace("CustomerCompany", description="Single namespace, single entity")


@api.route("/")
class CustomerCompanyResource(Resource):

    @responds(schema=CustomerCompanySchema(many=True))
    def get(self) -> List[CustomerCompany]:

        return CustomerCompaniesService.get_all()

    @accepts(schema=CustomerCompanySchema, api=api)
    @responds(schema=CustomerCompanySchema)
    def post(self) -> CustomerCompany:
        obj: dict = request.parsed_obj
        return CustomerCompanyService.create(obj)


@api.route("/<int:CompanyId>")
@api.param("CustomerCompaniesId", "CustomerCompany database ID")
class CustomerCompanyIdResource(Resource):
    @responds(schema=CustomerCompanySchema)
    def get(self, CompanyId: int) -> CustomerCompany:
        return CustomerCompaniesService.get_by_id(CompanyId)

    def delete(self, CompanyId: int) -> Response:
        from flask import jsonify

        id: int = CustomerCompaniesService.delete_by_id(CompanyId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CustomerCompanySchema, api=api)
    @responds(schema=CustomerCompanySchema)
    def put(self, CompanyId: int) -> CustomerCompany:

        changes: CustomerCompanyInterface = request.parsed_obj
        customercompany = CustomerCompaniesService.get_by_id(CustomerCompanies)
        return CustomerCompaniesService.update(customercompany, changes)

