from pytest import fixture

from .interface import PhoneNumberInterface
from .model import PhoneNumber
from .schema import PhoneNumberSchema


@fixture
def schema() -> PhoneNumberSchema:
    return PhoneNumberSchema()


def test_PhoneNumberSchema_create(schema: PhoneNumberSchema):
    assert schema


def test_PhoneNumberSchema_works(schema: PhoneNumberSchema):
    params: PhoneNumberInterface = schema.load(
        {"PeoplePersonId": 1, "LocationLocationId": 1, "PhoneNumber": 1, "CountryCode": 1, "PhoneType": 1}
    )
    phonenumber = PhoneNumber(**params)

    assert phonenumber.PeoplePersonId == 1
    assert phonenumber.LocationLocationId == 1
    assert phonenumber.PhoneNumber == 1
    assert phonenumber.CountryCode == 1
    assert phonenumber.PhoneType == 1
