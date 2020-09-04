from pytest import fixture
from .model import Employment
from .interface import EmploymentInterface


@fixture
def interface() -> EmploymentInterface:
    return EmploymentInterface(EmployeeId=1, PersonId=1, HRJobId=1, ManagerEmployeeId=1, StartDate="test", EndDate="test", Salary="test", CommissionPercent=1, EmploymentCol="test")


def test_EmploymentInterface_create(interface: EmploymentInterface):
    assert interface


def test_EmploymentInterface_works(interface: EmploymentInterface):
    employment = Employment(**interface)
    assert employment

