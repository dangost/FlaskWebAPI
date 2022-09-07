from pytest import fixture

from .interface import ProductInterface
from .model import Product
from .schema import ProductSchema


@fixture
def schema() -> ProductSchema:
    return ProductSchema()


def test_ProductSchema_create(schema: ProductSchema):
    assert schema


def test_ProductSchema_works(schema: ProductSchema):
    params: ProductInterface = schema.load(
        {"ProductName": "test", "Description": "test", "Category": 1, "WeightClass": "test", "WarrantyPeriod": 1,
         "SupplierId": 1, "Status": "test", "ListPrice": 1, "MinimumPrice": 1, "PriceCurrency": "test",
         "CatalogURL": "test"}
    )
    product = Product(**params)

    assert product.ProductName == "test"
    assert product.Description == "test"
    assert product.Category == 1
    assert product.WeightClass == "test"
    assert product.WarrantyPeriod == 1
    assert product.SupplierId == 1
    assert product.Status == "test"
    assert product.ListPrice == 1
    assert product.MinimumPrice == 1
    assert product.PriceCurrency == "test"
    assert product.CatalogURL == "test"
