from pytest import fixture
from .model import PhoneNumber
from .interface import PhoneNumberInterface


@fixture
def interface() -> PhoneNumberInterface:
    return PhoneNumberInterface(PhoneNumberId=1, PeoplePersonId=1, LocationLocationId=1, PhoneNumber=1, CountryCode=1, PhoneType=1)


def test_PhoneNumberInterface_create(interface: PhoneNumberInterface):
    assert interface


def test_PhoneNumberInterface_works(interface: PhoneNumberInterface):
    phonenumber = PhoneNumber(**interface)
    assert phonenumber

