from pytest import fixture
from .model import Person
from .interface import PersonInterface


@fixture
def interface() -> PersonInterface:
    return PersonInterface(PersonId=1, FirstName="test", LastName="test", MiddleName="test", Nickname="test", NatLangCode=1, CultureCode=1, Gender="test")


def test_PersonInterface_create(interface: PersonInterface):
    assert interface


def test_PersonInterface_works(interface: PersonInterface):
    person = Person(**interface)
    assert person

