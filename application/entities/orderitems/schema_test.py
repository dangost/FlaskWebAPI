from pytest import fixture

from .model import OrderItem
from .schema import OrderItemSchema
from .interface import OrderItemInterface


@fixture
def schema() -> OrderItemSchema:
    return OrderItemSchema()


def test_OrderItemSchema_create(schema: OrderItemSchema):
    assert schema


def test_OrderItemSchema_works(schema: OrderItemSchema):
    params: OrderItemInterface = schema.load(
        {"OrderId": 1, "ProductId": 1, "UnitPrice": 1, "Quantity": 1}
    )
    orderitem = OrderItem(**params)

    assert orderitem.OrderId == 1
    assert orderitem.ProductId == 1
    assert orderitem.UnitPrice == 1
    assert orderitem.Quantity == 1


