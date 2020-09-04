from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import WarehouseInterface


class Warehouse(db.Model):

    __tablename__ = "Warehouses"

    LocationId = Column(String(255))
    WarehouseName = Column(Integer())


    def update(self, changes: WarehouseInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



