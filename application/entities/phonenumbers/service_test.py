from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import PhoneNumber
from .service import PhoneNumbersService  # noqa
from .interface import PhoneNumberInterface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: PhoneNumber = PhoneNumber(PhoneNumberId=16, PeoplePersonId=16, LocationLocationId=16, PhoneNumber=16, CountryCode=16, PhoneType=16)
    yang: PhoneNumber = PhoneNumber(PhoneNumberId=16, PeoplePersonId=16, LocationLocationId=16, PhoneNumber=16, CountryCode=16, PhoneType=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[PhoneNumber] = PhoneNumbersService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: PhoneNumber = PhoneNumber(PhoneNumberId=16, PeoplePersonId=16, LocationLocationId=16, PhoneNumber=16, CountryCode=16, PhoneType=16)
    yang: PhoneNumber = PhoneNumber(PhoneNumberId=16, PeoplePersonId=16, LocationLocationId=16, PhoneNumber=16, CountryCode=16, PhoneType=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    PhoneNumbersService.delete_by_id(1)
    db.session.commit()

    results: List[PhoneNumber] = PhoneNumber.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: PhoneNumberInterface = dict(PeoplePersonId=1)
    PhoneNumbersService.create(yin)
    results: List[PhoneNumber] = PhoneNumber.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


