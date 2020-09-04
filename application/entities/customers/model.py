from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CustomerInterface


class Customer(db.Model):

    __tablename__ = "Customers"

    PersonId = Column(String(255))
    CustomEmployeeId = Column(String(255))
    AccountMgrId = Column(String(255))
    IncomeLevel = Column(String(255))


    def update(self, changes: CustomerInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



