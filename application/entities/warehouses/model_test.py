from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import Warehouse


@fixture
def warehouse() -> Warehouse:
    return Warehouse(WarehouseId=1, LocationId=1, WarehouseName="test")


def test_Warehouse_create(warehouse: Warehouse):
    assert warehouse


def test_Warehouse_retrieve(warehouse: Warehouse, db: SQLAlchemy):  # noqa
    db.session.add(warehouse)
    db.session.commit()
    s = Warehouse.query.first()
    assert s.__dict__ == warehouse.__dict__
