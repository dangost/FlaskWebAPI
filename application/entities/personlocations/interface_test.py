from pytest import fixture
from .model import PersonLocation
from .interface import PersonLocationInterface


@fixture
def interface() -> PersonLocationInterface:
    return PersonLocationInterface(PersonsPersonId=1, LocationsLocationsId=1, SubAddress="test", LocationUsage="test", Notes="test")


def test_PersonLocationInterface_create(interface: PersonLocationInterface):
    assert interface


def test_PersonLocationInterface_works(interface: PersonLocationInterface):
    personlocation = PersonLocation(**interface)
    assert personlocation

