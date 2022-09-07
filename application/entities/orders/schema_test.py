from pytest import fixture

from .interface import OrdersInterface
from .model import Orders
from .schema import OrdersSchema


@fixture
def schema() -> OrdersSchema:
    return OrdersSchema()


def test_OrdersSchema_create(schema: OrdersSchema):
    assert schema


def test_OrdersSchema_works(schema: OrdersSchema):
    params: OrdersInterface = schema.load(
        {"CustomerId": 1, "SalesRepId": 1, "OrderDate": "test", "OrderCode": "test", "OrderStatus": "test",
         "OrderTotal": 1, "OrderCurrency": "test", "PromotionCode": "test"}
    )
    orders = Orders(**params)

    assert orders.CustomerId == 1
    assert orders.SalesRepId == 1
    assert orders.OrderDate == "test"
    assert orders.OrderCode == "test"
    assert orders.OrderStatus == "test"
    assert orders.OrderTotal == 1
    assert orders.OrderCurrency == "test"
    assert orders.PromotionCode == "test"
