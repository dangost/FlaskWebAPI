from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Product
from .schema import ProductSchema
from .service import ProductsService


def make_product(
        productid: int = 1, productname: str = "test", description: str = "test", category: int = 1,
        weightclass: str = "test", warrantyperiod: int = 1, supplierid: int = 1, status: str = "test",
        listprice: int = 1, minimumprice: int = 1, pricecurrency: str = "test", catalogurl: str = "test"
) -> Product:
    return Product(ProductId=productid, ProductName=productname, Description=description, Category=category,
                   WeightClass=weightclass, WarrantyPeriod=warrantyperiod, SupplierId=supplierid, Status=status,
                   ListPrice=listprice, MinimumPrice=minimumprice, PriceCurrency=pricecurrency, CatalogURL=catalogurl)


class TestProductResource:
    @patch.object(
        ProductsService,
        "get_all",
        lambda: [
            make_product(),
            make_product(ProductId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                ProductSchema(many=True)
                    .dump(
                    [
                        make_product(),
                        make_product(ProductId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        ProductsService, "create", lambda create_request: Product(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(ProductName="test", Description="test", Category=1, WeightClass="test", WarrantyPeriod=1,
                           SupplierId=1, Status="test", ListPrice=1, MinimumPrice=1, PriceCurrency="test",
                           CatalogURL="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                ProductSchema()
                    .dump(Product(ProductName=payload["test"], Description=payload["test"], Category=payload[1],
                                  WeightClass=payload["test"], WarrantyPeriod=payload[1], SupplierId=payload[1],
                                  Status=payload["test"], ListPrice=payload[1], MinimumPrice=payload[1],
                                  PriceCurrency=payload["test"], CatalogURL=payload["test"]))

            )
            assert result == expected


class TestProductIdResource:
    @patch.object(ProductsService, "get_by_id", lambda id: make_product(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_product(id=123)
            print(f"result = ", result)
            assert result["ProductId"] == expected.ProductId

    @patch.object(ProductsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
