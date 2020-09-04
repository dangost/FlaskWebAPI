from pytest import fixture

from .model import PersonLocation
from .schema import PersonLocationSchema
from .interface import PersonLocationInterface


@fixture
def schema() -> PersonLocationSchema:
    return PersonLocationSchema()


def test_PersonLocationSchema_create(schema: PersonLocationSchema):
    assert schema


def test_PersonLocationSchema_works(schema: PersonLocationSchema):
    params: PersonLocationInterface = schema.load(
        {"PeoplePersonId": 1, "LocationsLocationsId": 1, "SubAddress": "test", "LocationUsage": "test", "Notes": "test"}
    )
    personlocation = PersonLocation(**params)

    assert personlocation.PeoplePersonId == 1
    assert personlocation.LocationsLocationsId == 1
    assert personlocation.SubAddress == "test"
    assert personlocation.LocationUsage == "test"
    assert personlocation.Notes == "test"


