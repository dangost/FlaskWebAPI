from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import InventoryInterface


class Inventory(db.Model):

    __tablename__ = "Inventories"

    ProductId = Column(String(255))
    WarehouseId = Column(String(255))
    QuantityOnHand = Column(String(255))
    QuantityAvaileble = Column(String(255))


    def update(self, changes: InventoryInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



