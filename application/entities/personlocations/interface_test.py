from pytest import fixture

from .interface import PersonLocationInterface
from .model import PersonLocation


@fixture
def interface() -> PersonLocationInterface:
    return PersonLocationInterface(PersonsPersonId=1, LocationsLocationsId=1, SubAddress="test", LocationUsage="test",
                                   Notes="test")


def test_PersonLocationInterface_create(interface: PersonLocationInterface):
    assert interface


def test_PersonLocationInterface_works(interface: PersonLocationInterface):
    personlocation = PersonLocation(**interface)
    assert personlocation
