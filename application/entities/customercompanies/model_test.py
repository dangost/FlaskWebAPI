from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import CustomerCompany


@fixture
def customercompany() -> CustomerCompany:
    return CustomerCompany(CompanyId=1, CompanyName="test", CompanyCreditLimit="test", CreditLimitCurrency="test")


def test_CustomerCompany_create(customercompany: CustomerCompany):
    assert customercompany


def test_CustomerCompany_retrieve(customercompany: CustomerCompany, db: SQLAlchemy):  # noqa
    db.session.add(customercompany)
    db.session.commit()
    s = CustomerCompany.query.first()
    assert s.__dict__ == customercompany.__dict__
