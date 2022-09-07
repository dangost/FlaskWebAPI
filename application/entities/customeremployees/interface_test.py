from pytest import fixture

from .interface import CustomerEmployeeInterface
from .model import CustomerEmployee


@fixture
def interface() -> CustomerEmployeeInterface:
    return CustomerEmployeeInterface(CustomerEmployeeId=1, CompanyId=1, BadgeNumber="test", JobTitle="test",
                                     Department="test", CreditLimit=1, CreditLimitCurrency=1)


def test_CustomerEmployeeInterface_create(interface: CustomerEmployeeInterface):
    assert interface


def test_CustomerEmployeeInterface_works(interface: CustomerEmployeeInterface):
    customeremployee = CustomerEmployee(**interface)
    assert customeremployee
