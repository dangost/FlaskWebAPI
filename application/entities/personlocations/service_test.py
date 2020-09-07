from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import PersonLocation
from .service import PersonLocationsService  # noqa
from .interface import PersonLocationInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: PersonLocation = PersonLocation(PersonsPersonId=16, LocationsLocationsId=16, SubAddress="test16", LocationUsage="test16", Notes="test16")
    yang: PersonLocation = PersonLocation(PersonsPersonId=16, LocationsLocationsId=16, SubAddress="test16", LocationUsage="test16", Notes="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[PersonLocation] = PersonLocationsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: PersonLocation = PersonLocation(PersonsPersonId=16, LocationsLocationsId=16, SubAddress="test16", LocationUsage="test16", Notes="test16")
    yang: PersonLocation = PersonLocation(PersonsPersonId=16, LocationsLocationsId=16, SubAddress="test16", LocationUsage="test16", Notes="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    PersonLocationsService.delete_by_id(1)
    db.session.commit()

    results: List[PersonLocation] = PersonLocation.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: PersonLocationInterface = dict(PeoplePersonId=1)
    PersonLocationsService.create(yin)
    results: List[PersonLocation] = PersonLocation.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


