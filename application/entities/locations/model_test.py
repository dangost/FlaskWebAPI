from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import Location


@fixture
def location() -> Location:
    return Location(LocationId=1, CountryId=1, AddressLine1="test", AddressLine2="test", City="test", State="test", District="test", PostalCode="test", LocationTypeCode=1, Description="test", ShippingNotes="test", CountriesCountryId=1)


def test_Location_create(location: Location):
    assert location


def test_Location_retrieve(location: Location, db: SQLAlchemy):  # noqa
    db.session.add(location)
    db.session.commit()
    s = Location.query.first()
    assert s.__dict__ == location.__dict__

