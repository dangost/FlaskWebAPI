from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import Customer


@fixture
def customer() -> Customer:
    return Customer(CustomerId=1, PersonId=1, CustomEmployeeId=1, AccountMgrId=1, IncomeLevel=1)


def test_Customer_create(customer: Customer):
    assert customer


def test_Customer_retrieve(customer: Customer, db: SQLAlchemy):  # noqa
    db.session.add(customer)
    db.session.commit()
    s = Customer.query.first()
    assert s.__dict__ == customer.__dict__
