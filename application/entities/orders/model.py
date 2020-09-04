from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import OrdersInterface


class Orders(db.Model):

    __tablename__ = "Orders"

    CustomerId = Column(String(255))
    SalesRepId = Column(String(255))
    OrderDate = Column(Integer())
    OrderCode = Column(Integer())
    OrderStatus = Column(Integer())
    OrderTotal = Column(String(255))
    OrderCurrency = Column(Integer())
    PromotionCode = Column(Integer())


    def update(self, changes: OrdersInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



