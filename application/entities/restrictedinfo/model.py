from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import RestrictedInfoInterface


class RestrictedInfo(db.Model):

    __tablename__ = "RestrictedInfo"

    PersonId = Column(Integer(), ForeignKey("People.PersonId"), primary_key=True)
    DateOfBirth = Column(String(255))
    DateOfDeath = Column(String(255))
    GovernmentId = Column(String(255))
    PassportId = Column(String(255))
    HireDire = Column(String(255))
    SeniorityCode = Column(Integer())


    def update(self, changes: RestrictedInfoInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



