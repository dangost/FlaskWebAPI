from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import CountryInterface
from .model import Country
from .service import CountriesService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Country = Country(CountryId=16, CountryName="test16", CountryCode="test16", NatLangCode=16,
                           CurrencyCode="test16")
    yang: Country = Country(CountryId=16, CountryName="test16", CountryCode="test16", NatLangCode=16,
                            CurrencyCode="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Country] = CountriesService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Country = Country(CountryId=16, CountryName="test16", CountryCode="test16", NatLangCode=16,
                           CurrencyCode="test16")
    yang: Country = Country(CountryId=16, CountryName="test16", CountryCode="test16", NatLangCode=16,
                            CurrencyCode="test16")
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    CountriesService.delete_by_id(1)
    db.session.commit()

    results: List[Country] = Country.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: CountryInterface = dict(CountryName="test")
    CountriesService.create(yin)
    results: List[Country] = Country.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
