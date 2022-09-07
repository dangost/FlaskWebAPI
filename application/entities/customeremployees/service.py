from typing import List

from application import db
from .interface import CustomerEmployeeInterface
from .model import CustomerEmployee


class CustomerEmployeesService:
    def get_all(self) -> List[CustomerEmployee]:
        return CustomerEmployee.query.all()

    def get_by_id(self, customeremployee_id: int) -> CustomerEmployee:
        return CustomerEmployee.query.get(customeremployee_id)

    def update(self, customeremployee: CustomerEmployee,
               customeremployee_change_updates: CustomerEmployeeInterface) -> CustomerEmployee:
        customeremployee.update(customeremployee_change_updates)
        db.session.commit()
        return customeremployee

    def delete_by_id(self, customeremployee_id: int) -> List[int]:
        customeremployee = CustomerEmployee.query.filter(
            CustomerEmployee.CustomerEmployeeId == customeremployee_id).first()
        if not customeremployee:
            return []
        db.session.delete(customeremployee)
        db.session.commit()
        return [customeremployee_id]

    def create(self, new_attrs: CustomerEmployeeInterface) -> CustomerEmployee:
        new_customeremployee = CustomerEmployee(CompanyId=new_attrs["CompanyId"], BadgeNumber=new_attrs["BadgeNumber"],
                                                JobTitle=new_attrs["JobTitle"], Department=new_attrs["Department"],
                                                CreditLimit=new_attrs["CreditLimit"],
                                                CreditLimitCurrency=new_attrs["CreditLimitCurrency"])
        db.session.add(new_customeremployee)
        db.session.commit()

        return new_customeremployee
