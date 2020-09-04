from pytest import fixture
from .model import RestrictedInfo
from .interface import RestrictedInfoInterface


@fixture
def interface() -> RestrictedInfoInterface:
    return RestrictedInfoInterface(PersonId=1, DateOfBirth="test", DateOfDeath="test", GovernmentId="test", PassportId="test", HireDire="test", SeniorityCode=1)


def test_RestrictedInfoInterface_create(interface: RestrictedInfoInterface):
    assert interface


def test_RestrictedInfoInterface_works(interface: RestrictedInfoInterface):
    restrictedinfo = RestrictedInfo(**interface)
    assert restrictedinfo

