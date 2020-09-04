from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import PersonInterface


class Person(db.Model):

    __tablename__ = "People"

    FirstName = Column(Integer())
    LastName = Column(Integer())
    MiddleName = Column(Integer())
    Nickname = Column(Integer())
    NatLangCode = Column(String(255))
    CultureCode = Column(String(255))
    Gender = Column(Integer())


    def update(self, changes: PersonInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



