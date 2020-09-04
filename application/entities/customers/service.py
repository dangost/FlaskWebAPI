from application import db
from typing import List
from .model import Customer
from .interface import CustomerInterface


class CustomersService:
    def get_all(self) -> List[Customer]:
        return Customer.query.all()

    def get_by_id(self, customer_id: int) -> Customer:
        return Customer.query.get(customer_id)

    def update(self, customer: Customer, customer_change_updates: CustomerInterface) -> Customer:
        customer.update(customer_change_updates)
        db.session.commit()
        return customer

    def delete_by_id(self, customer_id: int) -> List[int]:
        customer = Customer.query.filter(Customer.CustomerId == customer_id).first()
        if not customer:
            return []
        db.session.delete(customer)
        db.session.commit()
        return [customer_id]

    def create(self, new_attrs: CustomerInterface) -> Customer:
        new_customer = Customer(CustomerId=new_attrs["CustomerId"],  PersonId=new_attrs["PersonId"],  CustomEmployeeId=new_attrs["CustomEmployeeId"],  AccountMgrId=new_attrs["AccountMgrId"],  IncomeLevel=new_attrs["IncomeLevel"])
        db.session.add(new_customer)
        db.session.commit()

        return new_customer

