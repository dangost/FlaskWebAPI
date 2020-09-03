from sqlalchemy import Integer, Column, String
from application import db
from .interface import CountryInterface


class Country(db.Model):

    __tablename__ = "Countries"

    CountryId = Column(Integer(), primary_key=True)
    CountryName = Column(String(255))
    CountryCode = Column(String(255))
    NatLangCode = Column(Integer())
    CurrencyCode = Column(String(255))

    def update(self, changes: CountryInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self

