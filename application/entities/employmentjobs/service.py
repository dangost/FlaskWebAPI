from typing import List

from application import db
from .interface import EmploymentJobsInterface
from .model import EmploymentJobs


class EmploymentJobsService:
    def get_all(self) -> List[EmploymentJobs]:
        return EmploymentJobs.query.all()

    def get_by_id(self, employmentjobs_id: int) -> EmploymentJobs:
        return EmploymentJobs.query.get(employmentjobs_id)

    def update(self, employmentjobs: EmploymentJobs,
               employmentjobs_change_updates: EmploymentJobsInterface) -> EmploymentJobs:
        employmentjobs.update(employmentjobs_change_updates)
        db.session.commit()
        return employmentjobs

    def delete_by_id(self, employmentjobs_id: int) -> List[int]:
        employmentjobs = EmploymentJobs.query.filter(EmploymentJobs.HRJobId == employmentjobs_id).first()
        if not employmentjobs:
            return []
        db.session.delete(employmentjobs)
        db.session.commit()
        return [employmentjobs_id]

    def create(self, new_attrs: EmploymentJobsInterface) -> EmploymentJobs:
        new_employmentjobs = EmploymentJobs(CountriesCountryId=new_attrs["CountriesCountryId"],
                                            JobTitle=new_attrs["JobTitle"], MinSalary=new_attrs["MinSalary"],
                                            MaxSalary=new_attrs["MaxSalary"])
        db.session.add(new_employmentjobs)
        db.session.commit()

        return new_employmentjobs
