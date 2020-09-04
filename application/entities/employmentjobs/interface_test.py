from pytest import fixture
from .model import EmploymentJobs
from .interface import EmploymentJobsInterface


@fixture
def interface() -> EmploymentJobsInterface:
    return EmploymentJobsInterface(HRJobId=1, CountriesCountryId=1, JobTitle="test", MinSalary=1, MaxSalary=1)


def test_EmploymentJobsInterface_create(interface: EmploymentJobsInterface):
    assert interface


def test_EmploymentJobsInterface_works(interface: EmploymentJobsInterface):
    employmentjobs = EmploymentJobs(**interface)
    assert employmentjobs

