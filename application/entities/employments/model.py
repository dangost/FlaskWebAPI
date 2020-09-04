from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import EmploymentInterface


class Employment(db.Model):

    __tablename__ = "Employments"

    EmployeeId = Column(Integer(), primary_key=True)
    PersonId = Column(Integer(), ForeignKey("People.PersonId"))
    HRJobId = Column(Integer(), ForeignKey("EmploymentJobs.HRJobId"))
    ManagerEmployeeId = Column(Integer())
    StartDate = Column(String(255))
    EndDate = Column(String(255))
    Salary = Column(String(255))
    CommissionPercent = Column(Integer())
    EmploymentCol = Column(String(255))


    def update(self, changes: EmploymentInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



