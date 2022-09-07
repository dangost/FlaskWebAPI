from flask_sqlalchemy import SQLAlchemy
from typing import List

from .interface import LocationInterface
from .model import Location
from .service import LocationsService  # noqa


def test_get_all(db: SQLAlchemy):  # noqa
    yin: Location = Location(LocationId=16, CountryId=16, AddressLine1="test16", AddressLine2="test16", City="test16",
                             State="test16", District="test16", PostalCode="test16", LocationTypeCode=16,
                             Description="test16", ShippingNotes="test16", CountriesCountryId=16)
    yang: Location = Location(LocationId=16, CountryId=16, AddressLine1="test16", AddressLine2="test16", City="test16",
                              State="test16", District="test16", PostalCode="test16", LocationTypeCode=16,
                              Description="test16", ShippingNotes="test16", CountriesCountryId=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List[Location] = LocationsService.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: Location = Location(LocationId=16, CountryId=16, AddressLine1="test16", AddressLine2="test16", City="test16",
                             State="test16", District="test16", PostalCode="test16", LocationTypeCode=16,
                             Description="test16", ShippingNotes="test16", CountriesCountryId=16)
    yang: Location = Location(LocationId=16, CountryId=16, AddressLine1="test16", AddressLine2="test16", City="test16",
                              State="test16", District="test16", PostalCode="test16", LocationTypeCode=16,
                              Description="test16", ShippingNotes="test16", CountriesCountryId=16)
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    LocationsService.delete_by_id(1)
    db.session.commit()

    results: List[Location] = Location.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: LocationInterface = dict(CountryId=1)
    LocationsService.create(yin)
    results: List[Location] = Location.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]
