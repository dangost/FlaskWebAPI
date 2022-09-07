from pytest import fixture

from .interface import EmploymentJobsInterface
from .model import EmploymentJobs


@fixture
def interface() -> EmploymentJobsInterface:
    return EmploymentJobsInterface(HRJobId=1, CountriesCountryId=1, JobTitle="test", MinSalary=1, MaxSalary=1)


def test_EmploymentJobsInterface_create(interface: EmploymentJobsInterface):
    assert interface


def test_EmploymentJobsInterface_works(interface: EmploymentJobsInterface):
    employmentjobs = EmploymentJobs(**interface)
    assert employmentjobs
