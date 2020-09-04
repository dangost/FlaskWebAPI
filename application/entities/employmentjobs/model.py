from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import EmploymentJobsInterface


class EmploymentJobs(db.Model):

    __tablename__ = "EmploymentJobs"

    CountriesCountryId = Column(String(255))
    JobTitle = Column(Integer())
    MinSalary = Column(String(255))
    MaxSalary = Column(String(255))


    def update(self, changes: EmploymentJobsInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



