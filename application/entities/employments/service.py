from application import db
from typing import List
from .model import Employment
from .interface import EmploymentInterface


class EmploymentsService:
    def get_all(self) -> List[Employment]:
        return Employment.query.all()

    def get_by_id(self, employment_id: int) -> Employment:
        return Employment.query.get(employment_id)

    def update(self, employment: Employment, employment_change_updates: EmploymentInterface) -> Employment:
        employment.update(employment_change_updates)
        db.session.commit()
        return employment

    def delete_by_id(self, employment_id: int) -> List[int]:
        employment = Employment.query.filter(Employment.EmployeeID == employment_id).first()
        if not employment:
            return []
        db.session.delete(employment)
        db.session.commit()
        return [employment_id]

    def create(self, new_attrs: EmploymentInterface) -> Employment:
        new_employment = Employment(PersonId=new_attrs["PersonId"],  HRJobId=new_attrs["HRJobId"],  ManagerEmployeeId=new_attrs["ManagerEmployeeId"],  StartDate=new_attrs["StartDate"],  EndDate=new_attrs["EndDate"],  Salary=new_attrs["Salary"],  CommissionPercent=new_attrs["CommissionPercent"],  EmploymentCol=new_attrs["EmploymentCol"])
        db.session.add(new_employment)
        db.session.commit()

        return new_employment

