from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import EmploymentInterface


class Employment(db.Model):

    __tablename__ = "Employments"

    PersonId = Column(String(255))
    HRJobId = Column(String(255))
    ManagerEmployeeId = Column(String(255))
    StartDate = Column(Integer())
    EndDate = Column(Integer())
    Salary = Column(Integer())
    CommissionPercent = Column(String(255))
    Employmentcol = Column(Integer())


    def update(self, changes: EmploymentInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



