from pytest import fixture

from .interface import RestrictedInfoInterface
from .model import RestrictedInfo


@fixture
def interface() -> RestrictedInfoInterface:
    return RestrictedInfoInterface(PersonId=1, DateOfBirth="test", DateOfDeath="test", GovernmentId="test",
                                   PassportId="test", HireDire="test", SeniorityCode=1)


def test_RestrictedInfoInterface_create(interface: RestrictedInfoInterface):
    assert interface


def test_RestrictedInfoInterface_works(interface: RestrictedInfoInterface):
    restrictedinfo = RestrictedInfo(**interface)
    assert restrictedinfo
