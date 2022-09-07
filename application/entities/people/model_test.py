from flask_sqlalchemy import SQLAlchemy
from pytest import fixture

from application.test.fixtures import app, db  # noqa
from .model import Person


@fixture
def person() -> Person:
    return Person(PersonId=1, FirstName="test", LastName="test", MiddleName="test", Nickname="test", NatLangCode=1,
                  CultureCode=1, Gender="test")


def test_Person_create(person: Person):
    assert person


def test_Person_retrieve(person: Person, db: SQLAlchemy):  # noqa
    db.session.add(person)
    db.session.commit()
    s = Person.query.first()
    assert s.__dict__ == person.__dict__
