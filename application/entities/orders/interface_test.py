from pytest import fixture

from .interface import OrdersInterface
from .model import Orders


@fixture
def interface() -> OrdersInterface:
    return OrdersInterface(OrderId=1, CustomerId=1, SalesRepId=1, OrderDate="test", OrderCode="test",
                           OrderStatus="test", OrderTotal=1, OrderCurrency="test", PromotionCode="test")


def test_OrdersInterface_create(interface: OrdersInterface):
    assert interface


def test_OrdersInterface_works(interface: OrdersInterface):
    orders = Orders(**interface)
    assert orders
