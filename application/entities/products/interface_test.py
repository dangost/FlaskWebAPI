from pytest import fixture

from .interface import ProductInterface
from .model import Product


@fixture
def interface() -> ProductInterface:
    return ProductInterface(ProductId=1, ProductName="test", Description="test", Category=1, WeightClass="test",
                            WarrantyPeriod=1, SupplierId=1, Status="test", ListPrice=1, MinimumPrice=1,
                            PriceCurrency="test", CatalogURL="test")


def test_ProductInterface_create(interface: ProductInterface):
    assert interface


def test_ProductInterface_works(interface: ProductInterface):
    product = Product(**interface)
    assert product
