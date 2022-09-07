from typing import List

from application import db
from .interface import InventoryInterface
from .model import Inventory


class InventoriesService:
    def get_all(self) -> List[Inventory]:
        return Inventory.query.all()

    def get_by_id(self, inventory_id: int) -> Inventory:
        return Inventory.query.get(inventory_id)

    def update(self, inventory: Inventory, inventory_change_updates: InventoryInterface) -> Inventory:
        inventory.update(inventory_change_updates)
        db.session.commit()
        return inventory

    def delete_by_id(self, inventory_id: int) -> List[int]:
        inventory = Inventory.query.filter(Inventory.InventoryId == inventory_id).first()
        if not inventory:
            return []
        db.session.delete(inventory)
        db.session.commit()
        return [inventory_id]

    def create(self, new_attrs: InventoryInterface) -> Inventory:
        new_inventory = Inventory(ProductId=new_attrs["ProductId"], WarehouseId=new_attrs["WarehouseId"],
                                  QuantityOnHand=new_attrs["QuantityOnHand"],
                                  QuantityAvailable=new_attrs["QuantityAvailable"])
        db.session.add(new_inventory)
        db.session.commit()

        return new_inventory
