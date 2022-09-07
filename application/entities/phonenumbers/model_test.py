from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import PhoneNumber


@fixture
def phonenumber() -> PhoneNumber:
    return PhoneNumber(PhoneNumberId=1, PeoplePersonId=1, LocationLocationId=1, PhoneNumber=1, CountryCode=1,
                       PhoneType=1)


def test_PhoneNumber_create(phonenumber: PhoneNumber):
    assert phonenumber


def test_PhoneNumber_retrieve(phonenumber: PhoneNumber, db: SQLAlchemy):  # noqa
    db.session.add(phonenumber)
    db.session.commit()
    s = PhoneNumber.query.first()
    assert s.__dict__ == phonenumber.__dict__
