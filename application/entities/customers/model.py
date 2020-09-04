from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CustomerInterface


class Customer(db.Model):

    __tablename__ = "Customers"

    CustomerId = Column(Integer(), ForeignKey("Orders.CustomerId"), primary_key=True)
    PersonId = Column(Integer(), ForeignKey("People.PersonId"))
    CustomEmployeeId = Column(Integer(), ForeignKey("CustomerEmployees.CustomerEmployeeId"))
    AccountMgrId = Column(Integer())
    IncomeLevel = Column(Integer())


    def update(self, changes: CustomerInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



