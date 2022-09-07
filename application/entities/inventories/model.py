from sqlalchemy import Integer, Column, String, ForeignKey

from application import db
from .interface import InventoryInterface


class Inventory(db.Model):
    __tablename__ = "Inventories"

    InventoryId = Column(Integer(), primary_key=True)
    ProductId = Column(Integer(), ForeignKey("Products.ProductId"))
    WarehouseId = Column(Integer())
    QuantityOnHand = Column(Integer())
    QuantityAvailable = Column(Integer())

    def update(self, changes: InventoryInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
