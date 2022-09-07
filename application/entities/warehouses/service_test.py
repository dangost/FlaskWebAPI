from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import WarehouseInterface
from .model import Warehouse
from .service import WarehousesService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Warehouse = Warehouse(WarehouseId=16, LocationId=16, WarehouseName="test16")
    yang: Warehouse = Warehouse(WarehouseId=16, LocationId=16, WarehouseName="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Warehouse] = WarehousesService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Warehouse = Warehouse(WarehouseId=16, LocationId=16, WarehouseName="test16")
    yang: Warehouse = Warehouse(WarehouseId=16, LocationId=16, WarehouseName="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    WarehousesService.delete_by_id(1)
    db.session.commit()

    results: List[Warehouse] = Warehouse.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: WarehouseInterface = dict(WarehouseId=1)
    WarehousesService.create(yin)
    results: List[Warehouse] = Warehouse.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
