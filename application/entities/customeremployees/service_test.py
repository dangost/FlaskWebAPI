from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import CustomerEmployeeInterface
from .model import CustomerEmployee
from .service import CustomerEmployeesService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: CustomerEmployee = CustomerEmployee(CustomerEmployeeId=16, CompanyId=16, BadgeNumber="test16",
                                             JobTitle="test16", Department="test16", CreditLimit=16,
                                             CreditLimitCurrency=16)
    yang: CustomerEmployee = CustomerEmployee(CustomerEmployeeId=16, CompanyId=16, BadgeNumber="test16",
                                              JobTitle="test16", Department="test16", CreditLimit=16,
                                              CreditLimitCurrency=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[CustomerEmployee] = CustomerEmployeesService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: CustomerEmployee = CustomerEmployee(CustomerEmployeeId=16, CompanyId=16, BadgeNumber="test16",
                                             JobTitle="test16", Department="test16", CreditLimit=16,
                                             CreditLimitCurrency=16)
    yang: CustomerEmployee = CustomerEmployee(CustomerEmployeeId=16, CompanyId=16, BadgeNumber="test16",
                                              JobTitle="test16", Department="test16", CreditLimit=16,
                                              CreditLimitCurrency=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    CustomerEmployeesService.delete_by_id(1)
    db.session.commit()

    results: List[CustomerEmployee] = CustomerEmployee.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: CustomerEmployeeInterface = dict(CompanyId=1)
    CustomerEmployeesService.create(yin)
    results: List[CustomerEmployee] = CustomerEmployee.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
