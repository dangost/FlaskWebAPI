from pytest import fixture

from .interface import RestrictedInfoInterface
from .model import RestrictedInfo
from .schema import RestrictedInfoSchema


@fixture
def schema() -> RestrictedInfoSchema:
    return RestrictedInfoSchema()


def test_RestrictedInfoSchema_create(schema: RestrictedInfoSchema):
    assert schema


def test_RestrictedInfoSchema_works(schema: RestrictedInfoSchema):
    params: RestrictedInfoInterface = schema.load(
        {"PersonId": 1, "DateOfBirth": "test", "DateOfDeath": "test", "GovernmentId": "test", "PassportId": "test",
         "HireDire": "test", "SeniorityCode": 1}
    )
    restrictedinfo = RestrictedInfo(**params)

    assert restrictedinfo.PersonId == 1
    assert restrictedinfo.DateOfBirth == "test"
    assert restrictedinfo.DateOfDeath == "test"
    assert restrictedinfo.GovernmentId == "test"
    assert restrictedinfo.PassportId == "test"
    assert restrictedinfo.HireDire == "test"
    assert restrictedinfo.SeniorityCode == 1
