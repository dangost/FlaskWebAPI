from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import OrderItem
from .schema import OrderItemSchema
from .service import OrderItemsService


def make_orderitem(
        orderitemid: int = 1, orderid: int = 1, productid: int = 1, unitprice: int = 1, quantity: int = 1
) -> OrderItem:
    return OrderItem(OrderItemId=orderitemid, OrderId=orderid, ProductId=productid, UnitPrice=unitprice,
                     Quantity=quantity)


class TestOrderItemResource:
    @patch.object(
        OrderItemsService,
        "get_all",
        lambda: [
            make_orderitem(),
            make_orderitem(OrderItemId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                OrderItemSchema(many=True)
                    .dump(
                    [
                        make_orderitem(),
                        make_orderitem(OrderItemId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        OrderItemsService, "create", lambda create_request: OrderItem(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(OrderId=1, ProductId=1, UnitPrice=1, Quantity=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                OrderItemSchema()
                    .dump(
                    OrderItem(OrderId=payload[1], ProductId=payload[1], UnitPrice=payload[1], Quantity=payload[1]))

            )
            assert result == expected


class TestOrderItemIdResource:
    @patch.object(OrderItemsService, "get_by_id", lambda id: make_orderitem(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_orderitem(id=123)
            print(f"result = ", result)
            assert result["OrderItemId"] == expected.OrderItemId

    @patch.object(OrderItemsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
