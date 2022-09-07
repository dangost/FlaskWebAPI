from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import CustomerCompanyInterface
from .model import CustomerCompany
from .service import CustomerCompaniesService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: CustomerCompany = CustomerCompany(CompanyId=16, CompanyName="test16", CompanyCreditLimit="test16",
                                           CreditLimitCurrency="test16")
    yang: CustomerCompany = CustomerCompany(CompanyId=16, CompanyName="test16", CompanyCreditLimit="test16",
                                            CreditLimitCurrency="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[CustomerCompany] = CustomerCompaniesService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: CustomerCompany = CustomerCompany(CompanyId=16, CompanyName="test16", CompanyCreditLimit="test16",
                                           CreditLimitCurrency="test16")
    yang: CustomerCompany = CustomerCompany(CompanyId=16, CompanyName="test16", CompanyCreditLimit="test16",
                                            CreditLimitCurrency="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    CustomerCompaniesService.delete_by_id(1)
    db.session.commit()

    results: List[CustomerCompany] = CustomerCompany.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: CustomerCompanyInterface = dict(CompanyName="test")
    CustomerCompaniesService.create(yin)
    results: List[CustomerCompany] = CustomerCompany.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
