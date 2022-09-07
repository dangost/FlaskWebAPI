from sqlalchemy import Integer, Column, String, ForeignKey

from application import db
from .interface import CustomerCompanyInterface


class CustomerCompany(db.Model):
    __tablename__ = "CustomerCompanies"

    CompanyId = Column(Integer(), primary_key=True)
    CompanyName = Column(String(255))
    CompanyCreditLimit = Column(String(255))
    CreditLimitCurrency = Column(String(255))

    def update(self, changes: CustomerCompanyInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
