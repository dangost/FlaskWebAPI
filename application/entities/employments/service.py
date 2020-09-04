from application import db
from typing import List
from .model import Employment
from .interface import EmploymentInterface


class EmploymentsService:
    @staticmethod
    def get_all() -> List[Employment]:
        return Employment.query.all()

    @staticmethod
    def get_by_id(employment_id: int) -> Employment:
        return Employment.query.get(employment_id)

    @staticmethod
    def update(employment: Employment, employment_change_updates: EmploymentInterface) -> Employment:
        employment.update(employment_change_updates)
        db.session.commit()
        return employment

    @staticmethod
    def delete_by_id(employment_id: int) -> List[int]:
        employment = Employment.query.filter(Employment.EmployeeID == employment_id).first()
        if not employment:
            return []
        db.session.delete(employment)
        db.session.commit()
        return [employment_id]

    @staticmethod
    def create(new_attrs: EmploymentInterface) -> Employment:
        new_employment = Employment(PersonId=new_attrs["PersonId"],  HRJobId=new_attrs["HRJobId"],  ManagerEmployeeId=new_attrs["ManagerEmployeeId"],  StartDate=new_attrs["StartDate"],  EndDate=new_attrs["EndDate"],  Salary=new_attrs["Salary"],  CommissionPercent=new_attrs["CommissionPercent"],  Employmentcol=new_attrs["Employmentcol"])
        db.session.add(new_employment)
        db.session.commit()

        return new_employment

