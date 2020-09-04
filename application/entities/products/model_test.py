from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import Product


@fixture
def product() -> Product:
    return Product(ProductId=1, ProductName="test", Description="test", Category=1, WeightClass="test", WarrantyPeriod=1, SupplierId=1, Status="test", ListPrice=1, MinimumPrice=1, PriceCurrency="test", CatalogURL="test")


def test_Product_create(product: Product):
    assert product


def test_Product_retrieve(product: Product, db: SQLAlchemy):  # noqa
    db.session.add(product)
    db.session.commit()
    s = Product.query.first()
    assert s.__dict__ == product.__dict__

