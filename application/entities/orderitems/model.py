from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import OrderItemInterface


class OrderItem(db.Model):

    __tablename__ = "OrderItems"

    OrderId = Column(String(255))
    ProductId = Column(String(255))
    UnitPrice = Column(String(255))
    Quantity = Column(String(255))


    def update(self, changes: OrderItemInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



