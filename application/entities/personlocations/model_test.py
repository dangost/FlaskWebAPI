from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import PersonLocation


@fixture
def personlocation() -> PersonLocation:
    return PersonLocation(PersonsPersonId=1, LocationsLocationsId=1, SubAddress="test", LocationUsage="test",
                          Notes="test")


def test_PersonLocation_create(personlocation: PersonLocation):
    assert personlocation


def test_PersonLocation_retrieve(personlocation: PersonLocation, db: SQLAlchemy):  # noqa
    db.session.add(personlocation)
    db.session.commit()
    s = PersonLocation.query.first()
    assert s.__dict__ == personlocation.__dict__
