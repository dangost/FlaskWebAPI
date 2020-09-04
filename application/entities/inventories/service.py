from application import db
from typing import List
from .model import Inventory
from .interface import InventoryInterface


class InventoriesService:
    @staticmethod
    def get_all() -> List[Inventory]:
        return Inventory.query.all()

    @staticmethod
    def get_by_id(inventory_id: int) -> Inventory:
        return Inventory.query.get(inventory_id)

    @staticmethod
    def update(inventory: Inventory, inventory_change_updates: InventoryInterface) -> Inventory:
        inventory.update(inventory_change_updates)
        db.session.commit()
        return inventory

    @staticmethod
    def delete_by_id(inventory_id: int) -> List[int]:
        inventory = Inventory.query.filter(Inventory.InventoryId == inventory_id).first()
        if not inventory:
            return []
        db.session.delete(inventory)
        db.session.commit()
        return [inventory_id]

    @staticmethod
    def create(new_attrs: InventoryInterface) -> Inventory:
        new_inventory = Inventory(ProductId=new_attrs["ProductId"],  WarehouseId=new_attrs["WarehouseId"],  QuantityOnHand=new_attrs["QuantityOnHand"],  QuantityAvailable=new_attrs["QuantityAvailable"])
        db.session.add(new_inventory)
        db.session.commit()

        return new_inventory

