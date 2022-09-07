from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import RestrictedInfoInterface
from .model import RestrictedInfo
from .service import RestrictedInfoService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: RestrictedInfo = RestrictedInfo(PersonId=16, DateOfBirth="test16", DateOfDeath="test16", GovernmentId="test16",
                                         PassportId="test16", HireDire="test16", SeniorityCode=16)
    yang: RestrictedInfo = RestrictedInfo(PersonId=16, DateOfBirth="test16", DateOfDeath="test16",
                                          GovernmentId="test16", PassportId="test16", HireDire="test16",
                                          SeniorityCode=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[RestrictedInfo] = RestrictedInfoService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: RestrictedInfo = RestrictedInfo(PersonId=16, DateOfBirth="test16", DateOfDeath="test16", GovernmentId="test16",
                                         PassportId="test16", HireDire="test16", SeniorityCode=16)
    yang: RestrictedInfo = RestrictedInfo(PersonId=16, DateOfBirth="test16", DateOfDeath="test16",
                                          GovernmentId="test16", PassportId="test16", HireDire="test16",
                                          SeniorityCode=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    RestrictedInfoService.delete_by_id(1)
    db.session.commit()

    results: List[RestrictedInfo] = RestrictedInfo.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: RestrictedInfoInterface = dict(PersonId=1)
    RestrictedInfoService.create(yin)
    results: List[RestrictedInfo] = RestrictedInfo.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
