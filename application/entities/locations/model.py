from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import LocationInterface


class Location(db.Model):

    __tablename__ = "Locations"

    LocationId = Column(Integer(), primary_key=True)
    CountryId = Column(Integer(), ForeignKey("Countries.CountryId"))
    AddressLine1 = Column(String(255))
    AddressLine2 = Column(String(255))
    City = Column(String(255))
    State = Column(String(255))
    District = Column(String(255))
    PostalCode = Column(String(255))
    LocationTypeCode = Column(Integer())
    Description = Column(String(255))
    ShippingNotes = Column(String(255))
    CountriesCountryId = Column(Integer())


    def update(self, changes: LocationInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



