from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import PersonLocationInterface


class PersonLocation(db.Model):

    __tablename__ = "PersonLocations"

    LocationsLocationsId = Column(String(255))
    SubAdress = Column(Integer())
    LocationUsage = Column(Integer())
    Notes = Column(Integer())


    def update(self, changes: PersonLocationInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



