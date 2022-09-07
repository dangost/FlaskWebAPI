from sqlalchemy import Integer, Column, String, ForeignKey

from application import db
from .interface import PersonInterface


class Person(db.Model):
    __tablename__ = "People"

    PersonId = Column(Integer(), primary_key=True)
    FirstName = Column(String(255))
    LastName = Column(String(255))
    MiddleName = Column(String(255))
    Nickname = Column(String(255))
    NatLangCode = Column(Integer())
    CultureCode = Column(Integer())
    Gender = Column(String(255))

    def update(self, changes: PersonInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
