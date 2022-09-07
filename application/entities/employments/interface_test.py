from pytest import fixture

from .interface import EmploymentInterface
from .model import Employment


@fixture
def interface() -> EmploymentInterface:
    return EmploymentInterface(EmployeeId=1, PersonId=1, HRJobId=1, ManagerEmployeeId=1, StartDate="test",
                               EndDate="test", Salary="test", CommissionPercent=1, EmploymentCol="test")


def test_EmploymentInterface_create(interface: EmploymentInterface):
    assert interface


def test_EmploymentInterface_works(interface: EmploymentInterface):
    employment = Employment(**interface)
    assert employment
