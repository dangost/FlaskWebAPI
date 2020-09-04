from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import OrderItem


@fixture
def orderitem() -> OrderItem:
    return OrderItem(OrderItemId=1, OrderId=1, ProductId=1, UnitPrice=1, Quantity=1)


def test_OrderItem_create(orderitem: OrderItem):
    assert orderitem


def test_OrderItem_retrieve(orderitem: OrderItem, db: SQLAlchemy):  # noqa
    db.session.add(orderitem)
    db.session.commit()
    s = OrderItem.query.first()
    assert s.__dict__ == orderitem.__dict__

