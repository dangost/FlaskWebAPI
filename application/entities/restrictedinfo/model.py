from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import RestrictedInfoInterface


class RestrictedInfo(db.Model):

    __tablename__ = "RestrictedInfo"

    DateOfBirth = Column(Integer())
    DateOfDeath = Column(Integer())
    GovernmentId = Column(Integer())
    PassportId = Column(Integer())
    HireDire = Column(Integer())
    SeniorityCode = Column(String(255))


    def update(self, changes: RestrictedInfoInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



