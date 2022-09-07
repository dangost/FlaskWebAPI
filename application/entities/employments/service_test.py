from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import EmploymentInterface
from .model import Employment
from .service import EmploymentsService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Employment = Employment(EmployeeId=16, PersonId=16, HRJobId=16, ManagerEmployeeId=16, StartDate="test16",
                                 EndDate="test16", Salary="test16", CommissionPercent=16, EmploymentCol="test16")
    yang: Employment = Employment(EmployeeId=16, PersonId=16, HRJobId=16, ManagerEmployeeId=16, StartDate="test16",
                                  EndDate="test16", Salary="test16", CommissionPercent=16, EmploymentCol="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Employment] = EmploymentsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Employment = Employment(EmployeeId=16, PersonId=16, HRJobId=16, ManagerEmployeeId=16, StartDate="test16",
                                 EndDate="test16", Salary="test16", CommissionPercent=16, EmploymentCol="test16")
    yang: Employment = Employment(EmployeeId=16, PersonId=16, HRJobId=16, ManagerEmployeeId=16, StartDate="test16",
                                  EndDate="test16", Salary="test16", CommissionPercent=16, EmploymentCol="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    EmploymentsService.delete_by_id(1)
    db.session.commit()

    results: List[Employment] = Employment.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: EmploymentInterface = dict(PersonId=1)
    EmploymentsService.create(yin)
    results: List[Employment] = Employment.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
