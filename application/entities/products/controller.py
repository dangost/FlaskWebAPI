from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ProductSchema
from .service import ProductsService
from .model import Product
from .interface import ProductInterface

api = Namespace("Product", description="Single namespace, single entity")

service = ProductsService

@api.route("/")
class ProductResource(Resource):

    @responds(schema=ProductSchema(many=True))
    def get(self) -> List[Product]:
        
        return service.get_all(self)

    @accepts(schema=ProductSchema, api=api)
    @responds(schema=ProductSchema)
    def post(self) -> Product:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:ProductId>")
@api.param("ProductsId", "Product database ID")
class ProductIdResource(Resource):
    @responds(schema=ProductSchema)
    def get(self, ProductId: int) -> Product:
        return service.get_by_id(self, ProductId)

    def delete(self, ProductId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, ProductId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=ProductSchema, api=api)
    @responds(schema=ProductSchema)
    def put(self, ProductId: int) -> Product:

        changes: ProductInterface = request.parsed_obj
        product = service.get_by_id(self, ProductId)
        return service.update(self, product, changes)

