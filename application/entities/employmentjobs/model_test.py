from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import EmploymentJobs


@fixture
def employmentjobs() -> EmploymentJobs:
    return EmploymentJobs(HRJobId=1, CountriesCountryId=1, JobTitle="test", MinSalary=1, MaxSalary=1)


def test_EmploymentJobs_create(employmentjobs: EmploymentJobs):
    assert employmentjobs


def test_EmploymentJobs_retrieve(employmentjobs: EmploymentJobs, db: SQLAlchemy):  # noqa
    db.session.add(employmentjobs)
    db.session.commit()
    s = EmploymentJobs.query.first()
    assert s.__dict__ == employmentjobs.__dict__
