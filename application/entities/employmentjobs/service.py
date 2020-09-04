from application import db
from typing import List
from .model import EmploymentJobs
from .interface import EmploymentJobsInterface


class EmploymentJobsService:
    @staticmethod
    def get_all() -> List[EmploymentJobs]:
        return EmploymentJobs.query.all()

    @staticmethod
    def get_by_id(employmentjobs_id: int) -> EmploymentJobs:
        return EmploymentJobs.query.get(employmentjobs_id)

    @staticmethod
    def update(employmentjobs: EmploymentJobs, employmentjobs_change_updates: EmploymentJobsInterface) -> EmploymentJobs:
        employmentjobs.update(employmentjobs_change_updates)
        db.session.commit()
        return employmentjobs

    @staticmethod
    def delete_by_id(employmentjobs_id: int) -> List[int]:
        employmentjobs = EmploymentJobs.query.filter(EmploymentJobs.HRJobId == employmentjobs_id).first()
        if not employmentjobs:
            return []
        db.session.delete(employmentjobs)
        db.session.commit()
        return [employmentjobs_id]

    @staticmethod
    def create(new_attrs: EmploymentJobsInterface) -> EmploymentJobs:
        new_employmentjobs = EmploymentJobs(CountriesCountryId=new_attrs["CountriesCountryId"],  JobTitle=new_attrs["JobTitle"],  MinSalary=new_attrs["MinSalary"],  MaxSalary=new_attrs["MaxSalary"])
        db.session.add(new_employmentjobs)
        db.session.commit()

        return new_employmentjobs

