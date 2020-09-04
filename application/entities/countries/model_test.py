from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import Country


@fixture
def country() -> Country:
    return Country(CountryId=1, CountryName="test", CountryCode="test", NatLangCode=1, CurrencyCode="test")


def test_Country_create(country: Country):
    assert country


def test_Country_retrieve(country: Country, db: SQLAlchemy):  # noqa
    db.session.add(country)
    db.session.commit()
    s = Country.query.first()
    assert s.__dict__ == country.__dict__

