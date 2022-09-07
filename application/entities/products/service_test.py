from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import ProductInterface
from .model import Product
from .service import ProductsService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Product = Product(ProductId=16, ProductName="test16", Description="test16", Category=16, WeightClass="test16",
                           WarrantyPeriod=16, SupplierId=16, Status="test16", ListPrice=16, MinimumPrice=16,
                           PriceCurrency="test16", CatalogURL="test16")
    yang: Product = Product(ProductId=16, ProductName="test16", Description="test16", Category=16, WeightClass="test16",
                            WarrantyPeriod=16, SupplierId=16, Status="test16", ListPrice=16, MinimumPrice=16,
                            PriceCurrency="test16", CatalogURL="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Product] = ProductsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Product = Product(ProductId=16, ProductName="test16", Description="test16", Category=16, WeightClass="test16",
                           WarrantyPeriod=16, SupplierId=16, Status="test16", ListPrice=16, MinimumPrice=16,
                           PriceCurrency="test16", CatalogURL="test16")
    yang: Product = Product(ProductId=16, ProductName="test16", Description="test16", Category=16, WeightClass="test16",
                            WarrantyPeriod=16, SupplierId=16, Status="test16", ListPrice=16, MinimumPrice=16,
                            PriceCurrency="test16", CatalogURL="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    ProductsService.delete_by_id(1)
    db.session.commit()

    results: List[Product] = Product.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: ProductInterface = dict(ProductName="test")
    ProductsService.create(yin)
    results: List[Product] = Product.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
