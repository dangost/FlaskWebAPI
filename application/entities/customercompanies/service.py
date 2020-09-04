from application import db
from typing import List
from .model import CustomerCompany
from .interface import CustomerCompanyInterface


class CustomerCompaniesService:
    @staticmethod
    def get_all() -> List[CustomerCompany]:
        return CustomerCompany.query.all()

    @staticmethod
    def get_by_id(customercompany_id: int) -> CustomerCompany:
        return CustomerCompany.query.get(customercompany_id)

    @staticmethod
    def update(customercompany: CustomerCompany, customercompany_change_updates: CustomerCompanyInterface) -> CustomerCompany:
        customercompany.update(customercompany_change_updates)
        db.session.commit()
        return customercompany

    @staticmethod
    def delete_by_id(customercompany_id: int) -> List[int]:
        customercompany = CustomerCompany.query.filter(CustomerCompany.CompanyId == customercompany_id).first()
        if not customercompany:
            return []
        db.session.delete(customercompany)
        db.session.commit()
        return [customercompany_id]

    @staticmethod
    def create(new_attrs: CustomerCompanyInterface) -> CustomerCompany:
        new_customercompany = CustomerCompany(CompanyName=new_attrs["CompanyName"],  CompanyCreditLimit=new_attrs["CompanyCreditLimit"],  CreditLimitCurrency=new_attrs["CreditLimitCurrency"])
        db.session.add(new_customercompany)
        db.session.commit()

        return new_customercompany

