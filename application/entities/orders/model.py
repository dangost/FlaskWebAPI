from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import OrdersInterface


class Orders(db.Model):

    __tablename__ = "Orders"

    OrderId = Column(Integer(), primary_key=True)
    CustomerId = Column(Integer())
    SalesRepId = Column(Integer(), ForeignKey("CustomerCompanies.CompanyId"))
    OrderDate = Column(String(255))
    OrderCode = Column(String(255))
    OrderStatus = Column(String(255))
    OrderTotal = Column(Integer())
    OrderCurrency = Column(String(255))
    PromotionCode = Column(String(255))


    def update(self, changes: OrdersInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



