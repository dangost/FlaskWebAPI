from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import OrderItemInterface


class OrderItem(db.Model):

    __tablename__ = "OrderItems"

    OrderItemId = Column(Integer(), primary_key=True)
    OrderId = Column(Integer(), ForeignKey("Orders.OrderId"))
    ProductId = Column(Integer(), ForeignKey("Products.ProductId"))
    UnitPrice = Column(Integer())
    Quantity = Column(Integer())


    def update(self, changes: OrderItemInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



