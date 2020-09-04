from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import CountryInterface


class Country(db.Model):

    __tablename__ = "Countries"

    CountryName = Column(Integer())
    CountryCode = Column(Integer())
    NatLangCode = Column(String(255))
    CurrencyCode = Column(Integer())


    def update(self, changes: CountryInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



