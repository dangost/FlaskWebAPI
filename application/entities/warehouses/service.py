from application import db
from typing import List
from .model import Warehouse
from .interface import WarehouseInterface


class WarehousesService:
    @staticmethod
    def get_all() -> List[Warehouse]:
        return Warehouse.query.all()

    @staticmethod
    def get_by_id(warehouse_id: int) -> Warehouse:
        return Warehouse.query.get(warehouse_id)

    @staticmethod
    def update(warehouse: Warehouse, warehouse_change_updates: WarehouseInterface) -> Warehouse:
        warehouse.update(warehouse_change_updates)
        db.session.commit()
        return warehouse

    @staticmethod
    def delete_by_id(warehouse_id: int) -> List[int]:
        warehouse = Warehouse.query.filter(Warehouse.WarehouseId == warehouse_id).first()
        if not warehouse:
            return []
        db.session.delete(warehouse)
        db.session.commit()
        return [warehouse_id]

    @staticmethod
    def create(new_attrs: WarehouseInterface) -> Warehouse:
        new_warehouse = Warehouse(WarehouseId=new_attrs["WarehouseId"],  LocationId=new_attrs["LocationId"],  WarehouseName=new_attrs["WarehouseName"])
        db.session.add(new_warehouse)
        db.session.commit()

        return new_warehouse

