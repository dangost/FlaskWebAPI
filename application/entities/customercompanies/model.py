from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CustomerCompanyInterface


class CustomerCompany(db.Model):

    __tablename__ = "CustomerCompanies"

    CompanyName = Column(Integer())
    CompanyCreditLimit = Column(Integer())
    CreditLimitCurrency = Column(Integer())


    def update(self, changes: CustomerCompanyInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



