from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import EmploymentJobsInterface
from .model import EmploymentJobs
from .service import EmploymentJobsService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: EmploymentJobs = EmploymentJobs(HRJobId=16, CountriesCountryId=16, JobTitle="test16", MinSalary=16,
                                         MaxSalary=16)
    yang: EmploymentJobs = EmploymentJobs(HRJobId=16, CountriesCountryId=16, JobTitle="test16", MinSalary=16,
                                          MaxSalary=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[EmploymentJobs] = EmploymentJobsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: EmploymentJobs = EmploymentJobs(HRJobId=16, CountriesCountryId=16, JobTitle="test16", MinSalary=16,
                                         MaxSalary=16)
    yang: EmploymentJobs = EmploymentJobs(HRJobId=16, CountriesCountryId=16, JobTitle="test16", MinSalary=16,
                                          MaxSalary=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    EmploymentJobsService.delete_by_id(1)
    db.session.commit()

    results: List[EmploymentJobs] = EmploymentJobs.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: EmploymentJobsInterface = dict(CountriesCountryId=1)
    EmploymentJobsService.create(yin)
    results: List[EmploymentJobs] = EmploymentJobs.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
