from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CountrySchema
from .service import CountriesService
from .model import Country
from .interface import CountryInterface

api = Namespace("Country", description="Single namespace, single entity")


@api.route("/")
class CountryResource(Resource):

    @responds(schema=CountrySchema(many=True))
    def get(self) -> List[Country]:

        return CountriesService.get_all()

    @accepts(schema=CountrySchema, api=api)
    @responds(schema=CountrySchema)
    def post(self) -> Country:
        obj: dict = request.parsed_obj
        return CountryService.create(obj)


@api.route("/<int:CountryId>")
@api.param("CountriesId", "Country database ID")
class CountryIdResource(Resource):
    @responds(schema=CountrySchema)
    def get(self, CountryId: int) -> Country:
        return CountriesService.get_by_id(CountryId)

    def delete(self, CountryId: int) -> Response:
        from flask import jsonify

        id: int = CountriesService.delete_by_id(CountryId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CountrySchema, api=api)
    @responds(schema=CountrySchema)
    def put(self, CountryId: int) -> Country:

        changes: CountryInterface = request.parsed_obj
        country = CountriesService.get_by_id(Countries)
        return CountriesService.update(country, changes)

