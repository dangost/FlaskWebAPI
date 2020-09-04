from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import PhoneNumberInterface


class PhoneNumber(db.Model):

    __tablename__ = "PhoneNumbers"

    PeoplePersonId = Column(String(255))
    LocationLocationId = Column(String(255))
    Phonenumber = Column(String(255))
    CountryCode = Column(String(255))
    PhoneType = Column(String(255))


    def update(self, changes: PhoneNumberInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



