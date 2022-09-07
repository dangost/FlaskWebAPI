from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import InventoryInterface
from .model import Inventory
from .service import InventoriesService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Inventory = Inventory(InventoryId=16, ProductId=16, WarehouseId=16, QuantityOnHand=16, QuantityAvailable=16)
    yang: Inventory = Inventory(InventoryId=16, ProductId=16, WarehouseId=16, QuantityOnHand=16, QuantityAvailable=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Inventory] = InventoriesService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Inventory = Inventory(InventoryId=16, ProductId=16, WarehouseId=16, QuantityOnHand=16, QuantityAvailable=16)
    yang: Inventory = Inventory(InventoryId=16, ProductId=16, WarehouseId=16, QuantityOnHand=16, QuantityAvailable=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    InventoriesService.delete_by_id(1)
    db.session.commit()

    results: List[Inventory] = Inventory.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: InventoryInterface = dict(ProductId=1)
    InventoriesService.create(yin)
    results: List[Inventory] = Inventory.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
