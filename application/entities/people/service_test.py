from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import Person
from .service import PeopleService  # noqa
from .interface import PersonInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Person = Person(PersonId=16, FirstName="test16", LastName="test16", MiddleName="test16", Nickname="test16", NatLangCode=16, CultureCode=16, Gender="test16")
    yang: Person = Person(PersonId=16, FirstName="test16", LastName="test16", MiddleName="test16", Nickname="test16", NatLangCode=16, CultureCode=16, Gender="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Person] = PeopleService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Person = Person(PersonId=16, FirstName="test16", LastName="test16", MiddleName="test16", Nickname="test16", NatLangCode=16, CultureCode=16, Gender="test16")
    yang: Person = Person(PersonId=16, FirstName="test16", LastName="test16", MiddleName="test16", Nickname="test16", NatLangCode=16, CultureCode=16, Gender="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    PeopleService.delete_by_id(1)
    db.session.commit()

    results: List[Person] = Person.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: PersonInterface = dict(FirstName="test")
    PeopleService.create(yin)
    results: List[Person] = Person.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


