from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import WarehouseInterface


class Warehouse(db.Model):

    __tablename__ = "Warehouses"

    WarehouseId = Column(Integer(), ForeignKey("Inventories.WarehouseId"), primary_key=True)
    LocationId = Column(Integer(), ForeignKey("Locations.LocationId"))
    WarehouseName = Column(String(255))


    def update(self, changes: WarehouseInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



