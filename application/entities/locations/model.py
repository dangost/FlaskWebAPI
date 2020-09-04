from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import LocationInterface


class Location(db.Model):

    __tablename__ = "Locations"

    CountryId = Column(String(255))
    AdressLine1 = Column(Integer())
    AdressLine2 = Column(Integer())
    City = Column(Integer())
    State = Column(Integer())
    District = Column(Integer())
    PostalCode = Column(Integer())
    LocationTypeCode = Column(String(255))
    Description = Column(Integer())
    ShippingNotes = Column(Integer())
    CountriesCountryId = Column(String(255))


    def update(self, changes: LocationInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



