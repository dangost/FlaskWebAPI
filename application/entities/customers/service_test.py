from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import CustomerInterface
from .model import Customer
from .service import CustomersService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Customer = Customer(CustomerId=16, PersonId=16, CustomEmployeeId=16, AccountMgrId=16, IncomeLevel=16)
    yang: Customer = Customer(CustomerId=16, PersonId=16, CustomEmployeeId=16, AccountMgrId=16, IncomeLevel=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Customer] = CustomersService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Customer = Customer(CustomerId=16, PersonId=16, CustomEmployeeId=16, AccountMgrId=16, IncomeLevel=16)
    yang: Customer = Customer(CustomerId=16, PersonId=16, CustomEmployeeId=16, AccountMgrId=16, IncomeLevel=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    CustomersService.delete_by_id(1)
    db.session.commit()

    results: List[Customer] = Customer.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: CustomerInterface = dict(CustomerId=1)
    CustomersService.create(yin)
    results: List[Customer] = Customer.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
