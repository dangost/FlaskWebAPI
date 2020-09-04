from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CustomerEmployeeInterface


class CustomerEmployee(db.Model):

    __tablename__ = "CustomerEmployees"

    CustomerEmployeeId = Column(Integer(), primary_key= True)
    CompanyId = Column(Integer(), ForeignKey('CustomerCompanies.CompanyId'))
    BadgeNumber = Column(String(255))
    JobTitle = Column(String(255))
    Department = Column(String(255))
    CreditLimit = Column(Integer())
    CreditLimitCurrency = Column(Integer())


    def update(self, changes: CustomerEmployeeInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



