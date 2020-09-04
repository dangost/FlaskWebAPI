from pytest import fixture
from .model import CustomerCompany
from .interface import CustomerCompanyInterface


@fixture
def interface() -> CustomerCompanyInterface:
    return CustomerCompanyInterface(CompanyId=1, CompanyName="test", CompanyCreditLimit="test", CreditLimitCurrency="test")


def test_CustomerCompanyInterface_create(interface: CustomerCompanyInterface):
    assert interface


def test_CustomerCompanyInterface_works(interface: CustomerCompanyInterface):
    customercompany = CustomerCompany(**interface)
    assert customercompany

