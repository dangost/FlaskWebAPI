from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import Inventory


@fixture
def inventory() -> Inventory:
    return Inventory(InventoryId=1, ProductId=1, WarehouseId=1, QuantityOnHand=1, QuantityAvailable=1)


def test_Inventory_create(inventory: Inventory):
    assert inventory


def test_Inventory_retrieve(inventory: Inventory, db: SQLAlchemy):  # noqa
    db.session.add(inventory)
    db.session.commit()
    s = Inventory.query.first()
    assert s.__dict__ == inventory.__dict__

