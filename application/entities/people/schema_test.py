from pytest import fixture

from .model import Person
from .schema import PersonSchema
from .interface import PersonInterface


@fixture
def schema() -> PersonSchema:
    return PersonSchema()


def test_PersonSchema_create(schema: PersonSchema):
    assert schema


def test_PersonSchema_works(schema: PersonSchema):
    params: PersonInterface = schema.load(
        {"FirstName": "test", "LastName": "test", "MiddleName": "test", "Nickname": "test", "NatLangCode": 1, "CultureCode": 1, "Gender": "test"}
    )
    person = Person(**params)

    assert person.FirstName == "test"
    assert person.LastName == "test"
    assert person.MiddleName == "test"
    assert person.Nickname == "test"
    assert person.NatLangCode == 1
    assert person.CultureCode == 1
    assert person.Gender == "test"


