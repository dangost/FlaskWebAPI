from typing import List

from application import db
from .interface import CustomerCompanyInterface
from .model import CustomerCompany


class CustomerCompaniesService:
    def get_all(self) -> List[CustomerCompany]:
        return CustomerCompany.query.all()

    def get_by_id(self, customercompany_id: int) -> CustomerCompany:
        return CustomerCompany.query.get(customercompany_id)

    def update(self, customercompany: CustomerCompany,
               customercompany_change_updates: CustomerCompanyInterface) -> CustomerCompany:
        customercompany.update(customercompany_change_updates)
        db.session.commit()
        return customercompany

    def delete_by_id(self, customercompany_id: int) -> List[int]:
        customercompany = CustomerCompany.query.filter(CustomerCompany.CompanyId == customercompany_id).first()
        if not customercompany:
            return []
        db.session.delete(customercompany)
        db.session.commit()
        return [customercompany_id]

    def create(self, new_attrs: CustomerCompanyInterface) -> CustomerCompany:
        new_customercompany = CustomerCompany(CompanyName=new_attrs["CompanyName"],
                                              CompanyCreditLimit=new_attrs["CompanyCreditLimit"],
                                              CreditLimitCurrency=new_attrs["CreditLimitCurrency"])
        db.session.add(new_customercompany)
        db.session.commit()

        return new_customercompany
