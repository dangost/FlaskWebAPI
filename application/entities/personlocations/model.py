from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import PersonLocationInterface


class PersonLocation(db.Model):

    __tablename__ = "PersonLocations"

    PersonsPersonId = Column(Integer(), ForeignKey("People.PersonId"), primary_key=True)
    LocationsLocationsId = Column(Integer(), ForeignKey("Locations.LocationId"))
    SubAddress = Column(String(255))
    LocationUsage = Column(String(255))
    Notes = Column(String(255))


    def update(self, changes: PersonLocationInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



