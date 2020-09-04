from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import Employment


@fixture
def employment() -> Employment:
    return Employment(EmployeeId=1, PersonId=1, HRJobId=1, ManagerEmployeeId=1, StartDate="test", EndDate="test", Salary="test", CommissionPercent=1, EmploymentCol="test")


def test_Employment_create(employment: Employment):
    assert employment


def test_Employment_retrieve(employment: Employment, db: SQLAlchemy):  # noqa
    db.session.add(employment)
    db.session.commit()
    s = Employment.query.first()
    assert s.__dict__ == employment.__dict__

