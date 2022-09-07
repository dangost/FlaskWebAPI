from typing import List

from application import db
from .interface import WarehouseInterface
from .model import Warehouse


class WarehousesService:
    def get_all(self) -> List[Warehouse]:
        return Warehouse.query.all()

    def get_by_id(self, warehouse_id: int) -> Warehouse:
        return Warehouse.query.get(warehouse_id)

    def update(self, warehouse: Warehouse, warehouse_change_updates: WarehouseInterface) -> Warehouse:
        warehouse.update(warehouse_change_updates)
        db.session.commit()
        return warehouse

    def delete_by_id(self, warehouse_id: int) -> List[int]:
        warehouse = Warehouse.query.filter(Warehouse.WarehouseId == warehouse_id).first()
        if not warehouse:
            return []
        db.session.delete(warehouse)
        db.session.commit()
        return [warehouse_id]

    def create(self, new_attrs: WarehouseInterface) -> Warehouse:
        new_warehouse = Warehouse(WarehouseId=new_attrs["WarehouseId"], LocationId=new_attrs["LocationId"],
                                  WarehouseName=new_attrs["WarehouseName"])
        db.session.add(new_warehouse)
        db.session.commit()

        return new_warehouse
