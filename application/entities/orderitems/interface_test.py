from pytest import fixture

from .interface import OrderItemInterface
from .model import OrderItem


@fixture
def interface() -> OrderItemInterface:
    return OrderItemInterface(OrderItemId=1, OrderId=1, ProductId=1, UnitPrice=1, Quantity=1)


def test_OrderItemInterface_create(interface: OrderItemInterface):
    assert interface


def test_OrderItemInterface_works(interface: OrderItemInterface):
    orderitem = OrderItem(**interface)
    assert orderitem
