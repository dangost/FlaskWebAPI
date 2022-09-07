from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import Orders


@fixture
def orders() -> Orders:
    return Orders(OrderId=1, CustomerId=1, SalesRepId=1, OrderDate="test", OrderCode="test", OrderStatus="test",
                  OrderTotal=1, OrderCurrency="test", PromotionCode="test")


def test_Orders_create(orders: Orders):
    assert orders


def test_Orders_retrieve(orders: Orders, db: SQLAlchemy):  # noqa
    db.session.add(orders)
    db.session.commit()
    s = Orders.query.first()
    assert s.__dict__ == orders.__dict__
