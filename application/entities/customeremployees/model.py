from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CustomerEmployeeInterface


class CustomerEmployee(db.Model):

    __tablename__ = "CustomerEmployees"

    CompanyId = Column(String(255))
    BadgeNumber = Column(Integer())
    JobTitle = Column(Integer())
    Department = Column(Integer())
    CreditLimit = Column(String(255))
    CreditLimitCurrency = Column(String(255))


    def update(self, changes: CustomerEmployeeInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



