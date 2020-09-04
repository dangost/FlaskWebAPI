from pytest import fixture
from .model import Location
from .interface import LocationInterface


@fixture
def interface() -> LocationInterface:
    return LocationInterface(LocationId=1, CountryId=1, AddressLine1="test", AddressLine2="test", City="test", State="test", District="test", PostalCode="test", LocationTypeCode=1, Description="test", ShippingNotes="test", CountriesCountryId=1)


def test_LocationInterface_create(interface: LocationInterface):
    assert interface


def test_LocationInterface_works(interface: LocationInterface):
    location = Location(**interface)
    assert location

