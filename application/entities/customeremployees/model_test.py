from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import CustomerEmployee


@fixture
def customeremployee() -> CustomerEmployee:
    return CustomerEmployee(CustomerEmployeeId=1, CompanyId=1, BadgeNumber="test", JobTitle="test", Department="test",
                            CreditLimit=1, CreditLimitCurrency=1)


def test_CustomerEmployee_create(customeremployee: CustomerEmployee):
    assert customeremployee


def test_CustomerEmployee_retrieve(customeremployee: CustomerEmployee, db: SQLAlchemy):  # noqa
    db.session.add(customeremployee)
    db.session.commit()
    s = CustomerEmployee.query.first()
    assert s.__dict__ == customeremployee.__dict__
