from pytest import fixture

from .interface import EmploymentJobsInterface
from .model import EmploymentJobs
from .schema import EmploymentJobsSchema


@fixture
def schema() -> EmploymentJobsSchema:
    return EmploymentJobsSchema()


def test_EmploymentJobsSchema_create(schema: EmploymentJobsSchema):
    assert schema


def test_EmploymentJobsSchema_works(schema: EmploymentJobsSchema):
    params: EmploymentJobsInterface = schema.load(
        {"CountriesCountryId": 1, "JobTitle": "test", "MinSalary": 1, "MaxSalary": 1}
    )
    employmentjobs = EmploymentJobs(**params)

    assert employmentjobs.CountriesCountryId == 1
    assert employmentjobs.JobTitle == "test"
    assert employmentjobs.MinSalary == 1
    assert employmentjobs.MaxSalary == 1
