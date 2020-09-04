from pytest import fixture

from .model import Employment
from .schema import EmploymentSchema
from .interface import EmploymentInterface


@fixture
def schema() -> EmploymentSchema:
    return EmploymentSchema()


def test_EmploymentSchema_create(schema: EmploymentSchema):
    assert schema


def test_EmploymentSchema_works(schema: EmploymentSchema):
    params: EmploymentInterface = schema.load(
        {"PersonId": 1, "HRJobId": 1, "ManagerEmployeeId": 1, "StartDate": "test", "EndDate": "test", "Salary": "test", "CommissionPercent": 1, "EmploymentCol": "test"}
    )
    employment = Employment(**params)

    assert employment.PersonId == 1
    assert employment.HRJobId == 1
    assert employment.ManagerEmployeeId == 1
    assert employment.StartDate == "test"
    assert employment.EndDate == "test"
    assert employment.Salary == "test"
    assert employment.CommissionPercent == 1
    assert employment.EmploymentCol == "test"


