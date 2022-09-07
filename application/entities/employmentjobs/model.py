from sqlalchemy import Integer, Column, String, ForeignKey

from application import db
from .interface import EmploymentJobsInterface


class EmploymentJobs(db.Model):
    __tablename__ = "EmploymentJobs"

    HRJobId = Column(Integer(), primary_key=True)
    CountriesCountryId = Column(Integer(), ForeignKey("Countries.CountryId"))
    JobTitle = Column(String(255))
    MinSalary = Column(Integer())
    MaxSalary = Column(Integer())

    def update(self, changes: EmploymentJobsInterface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self
