from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import Orders
from .service import OrdersService  # noqa
from .interface import OrdersInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Orders = Orders(OrderId=16, CustomerId=16, SalesRepId=16, OrderDate="test16", OrderCode="test16", OrderStatus="test16", OrderTotal=16, OrderCurrency="test16", PromotionCode="test16")
    yang: Orders = Orders(OrderId=16, CustomerId=16, SalesRepId=16, OrderDate="test16", OrderCode="test16", OrderStatus="test16", OrderTotal=16, OrderCurrency="test16", PromotionCode="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Orders] = OrdersService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Orders = Orders(OrderId=16, CustomerId=16, SalesRepId=16, OrderDate="test16", OrderCode="test16", OrderStatus="test16", OrderTotal=16, OrderCurrency="test16", PromotionCode="test16")
    yang: Orders = Orders(OrderId=16, CustomerId=16, SalesRepId=16, OrderDate="test16", OrderCode="test16", OrderStatus="test16", OrderTotal=16, OrderCurrency="test16", PromotionCode="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    OrdersService.delete_by_id(1)
    db.session.commit()

    results: List[Orders] = Orders.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: OrdersInterface = dict(CustomerId=1)
    OrdersService.create(yin)
    results: List[Orders] = Orders.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


