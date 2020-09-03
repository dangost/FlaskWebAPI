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


@api.route("/")
class ProductResource(Resource):

    @responds(schema=ProductSchema(many=True))
    def get(self) -> List[Product]:

        return ProductsService.get_all()

    @accepts(schema=ProductSchema, api=api)
    @responds(schema=ProductSchema)
    def post(self) -> Product:
        obj: dict = request.parsed_obj
        return ProductService.create(obj)


@api.route("/<int:ProductId>")
@api.param("ProductsId", "Product database ID")
class ProductIdResource(Resource):
    @responds(schema=ProductSchema)
    def get(self, ProductId: int) -> ProductId:
        return ProductsService.get_by_id(Products)

    def delete(self, ProductId: int) -> Response:
        from flask import jsonify

        id: int = ProductsService.delete_by_id(ProductId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=ProductSchema, api=api)
    @responds(schema=ProductSchema)
    def put(self, ProductId: int) -> Product:

        changes: ProductInterface = request.parsed_obj
        product = ProductsService.get_by_id(Products)
        return ProductsService.update(product, changes)

