from pytest import fixture

from .interface import LocationInterface
from .model import Location
from .schema import LocationSchema


@fixture
def schema() -> LocationSchema:
    return LocationSchema()


def test_LocationSchema_create(schema: LocationSchema):
    assert schema


def test_LocationSchema_works(schema: LocationSchema):
    params: LocationInterface = schema.load(
        {"CountryId": 1, "AddressLine1": "test", "AddressLine2": "test", "City": "test", "State": "test",
         "District": "test", "PostalCode": "test", "LocationTypeCode": 1, "Description": "test",
         "ShippingNotes": "test", "CountriesCountryId": 1}
    )
    location = Location(**params)

    assert location.CountryId == 1
    assert location.AddressLine1 == "test"
    assert location.AddressLine2 == "test"
    assert location.City == "test"
    assert location.State == "test"
    assert location.District == "test"
    assert location.PostalCode == "test"
    assert location.LocationTypeCode == 1
    assert location.Description == "test"
    assert location.ShippingNotes == "test"
    assert location.CountriesCountryId == 1
