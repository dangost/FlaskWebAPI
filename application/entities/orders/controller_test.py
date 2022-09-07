from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Orders
from .schema import OrdersSchema
from .service import OrdersService


def make_orders(
        orderid: int = 1, customerid: int = 1, salesrepid: int = 1, orderdate: str = "test", ordercode: str = "test",
        orderstatus: str = "test", ordertotal: int = 1, ordercurrency: str = "test", promotioncode: str = "test"
) -> Orders:
    return Orders(OrderId=orderid, CustomerId=customerid, SalesRepId=salesrepid, OrderDate=orderdate,
                  OrderCode=ordercode, OrderStatus=orderstatus, OrderTotal=ordertotal, OrderCurrency=ordercurrency,
                  PromotionCode=promotioncode)


class TestOrdersResource:
    @patch.object(
        OrdersService,
        "get_all",
        lambda: [
            make_orders(),
            make_orders(OrderId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                OrdersSchema(many=True)
                    .dump(
                    [
                        make_orders(),
                        make_orders(OrderId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        OrdersService, "create", lambda create_request: Orders(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(CustomerId=1, SalesRepId=1, OrderDate="test", OrderCode="test", OrderStatus="test",
                           OrderTotal=1, OrderCurrency="test", PromotionCode="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                OrdersSchema()
                    .dump(Orders(CustomerId=payload[1], SalesRepId=payload[1], OrderDate=payload["test"],
                                 OrderCode=payload["test"], OrderStatus=payload["test"], OrderTotal=payload[1],
                                 OrderCurrency=payload["test"], PromotionCode=payload["test"]))

            )
            assert result == expected


class TestOrdersIdResource:
    @patch.object(OrdersService, "get_by_id", lambda id: make_orders(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_orders(id=123)
            print(f"result = ", result)
            assert result["OrderId"] == expected.OrderId

    @patch.object(OrdersService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
