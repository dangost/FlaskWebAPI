from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import RestrictedInfo


@fixture
def restrictedinfo() -> RestrictedInfo:
    return RestrictedInfo(PersonId=1, DateOfBirth="test", DateOfDeath="test", GovernmentId="test", PassportId="test",
                          HireDire="test", SeniorityCode=1)


def test_RestrictedInfo_create(restrictedinfo: RestrictedInfo):
    assert restrictedinfo


def test_RestrictedInfo_retrieve(restrictedinfo: RestrictedInfo, db: SQLAlchemy):  # noqa
    db.session.add(restrictedinfo)
    db.session.commit()
    s = RestrictedInfo.query.first()
    assert s.__dict__ == restrictedinfo.__dict__
