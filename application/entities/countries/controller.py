from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

from .interface import CountryInterface
from .model import Country
from .schema import CountrySchema
from .service import CountriesService

api = Namespace("Country", description="Single namespace, single entity")

service = CountriesService


@api.route("/")
class CountryResource(Resource):

    @responds(schema=CountrySchema(many=True))
    def get(self) -> List[Country]:
        return service.get_all(self)

    @accepts(schema=CountrySchema, api=api)
    @responds(schema=CountrySchema)
    def post(self) -> Country:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:CountryId>")
@api.param("CountriesId", "Country database ID")
class CountryIdResource(Resource):
    @responds(schema=CountrySchema)
    def get(self, CountryId: int) -> Country:
        return service.get_by_id(self, CountryId)

    def delete(self, CountryId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, CountryId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CountrySchema, api=api)
    @responds(schema=CountrySchema)
    def put(self, CountryId: int) -> Country:
        changes: CountryInterface = request.parsed_obj
        country = service.get_by_id(self, CountryId)
        return service.update(self, country, changes)
