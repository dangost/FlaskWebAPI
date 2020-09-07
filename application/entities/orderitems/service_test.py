from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import OrderItem
from .service import OrderItemsService  # noqa
from .interface import OrderItemInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: OrderItem = OrderItem(OrderItemId=16, OrderId=16, ProductId=16, UnitPrice=16, Quantity=16)
    yang: OrderItem = OrderItem(OrderItemId=16, OrderId=16, ProductId=16, UnitPrice=16, Quantity=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[OrderItem] = OrderItemsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: OrderItem = OrderItem(OrderItemId=16, OrderId=16, ProductId=16, UnitPrice=16, Quantity=16)
    yang: OrderItem = OrderItem(OrderItemId=16, OrderId=16, ProductId=16, UnitPrice=16, Quantity=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    OrderItemsService.delete_by_id(1)
    db.session.commit()

    results: List[OrderItem] = OrderItem.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: OrderItemInterface = dict(OrderId=1)
    OrderItemsService.create(yin)
    results: List[OrderItem] = OrderItem.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


