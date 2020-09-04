from application import db
from typing import List
from .model import CustomerEmployee
from .interface import CustomerEmployeeInterface


class CustomerEmployeesService:
    @staticmethod
    def get_all() -> List[CustomerEmployee]:
        return CustomerEmployee.query.all()

    @staticmethod
    def get_by_id(customeremployee_id: int) -> CustomerEmployee:
        return CustomerEmployee.query.get(customeremployee_id)

    @staticmethod
    def update(customeremployee: CustomerEmployee, customeremployee_change_updates: CustomerEmployeeInterface) -> CustomerEmployee:
        customeremployee.update(customeremployee_change_updates)
        db.session.commit()
        return customeremployee

    @staticmethod
    def delete_by_id(customeremployee_id: int) -> List[int]:
        customeremployee = CustomerEmployee.query.filter(CustomerEmployee.CustomerEmployeeId == customeremployee_id).first()
        if not customeremployee:
            return []
        db.session.delete(customeremployee)
        db.session.commit()
        return [customeremployee_id]

    @staticmethod
    def create(new_attrs: CustomerEmployeeInterface) -> CustomerEmployee:
        new_customeremployee = CustomerEmployee(CompanyId=new_attrs["CompanyId"],  BadgeNumber=new_attrs["BadgeNumber"],  JobTitle=new_attrs["JobTitle"],  Department=new_attrs["Department"],  CreditLimit=new_attrs["CreditLimit"],  CreditLimitCurrency=new_attrs["CreditLimitCurrency"])
        db.session.add(new_customeremployee)
        db.session.commit()

        return new_customeremployee

