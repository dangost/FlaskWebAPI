from pytest import fixture
from .model import Customer
from .interface import CustomerInterface


@fixture
def interface() -> CustomerInterface:
    return CustomerInterface(CustomerId=1, PersonId=1, CustomEmployeeId=1, AccountMgrId=1, IncomeLevel=1)


def test_CustomerInterface_create(interface: CustomerInterface):
    assert interface


def test_CustomerInterface_works(interface: CustomerInterface):
    customer = Customer(**interface)
    assert customer

