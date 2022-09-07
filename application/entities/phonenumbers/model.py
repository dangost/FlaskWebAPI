from sqlalchemy import Integer, Column, String, ForeignKey

from application import db
from .interface import PhoneNumberInterface


class PhoneNumber(db.Model):
    __tablename__ = "PhoneNumbers"

    PhoneNumberId = Column(Integer(), primary_key=True)
    PeoplePersonId = Column(Integer(), ForeignKey("People.PersonId"))
    LocationLocationId = Column(Integer(), ForeignKey("Locations.LocationId"))
    PhoneNumber = Column(Integer())
    CountryCode = Column(Integer())
    PhoneType = Column(Integer())

    def update(self, changes: PhoneNumberInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
