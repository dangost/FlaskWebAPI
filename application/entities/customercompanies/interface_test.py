from pytest import fixture

from .interface import CustomerCompanyInterface
from .model import CustomerCompany


@fixture
def interface() -> CustomerCompanyInterface:
    return CustomerCompanyInterface(CompanyId=1, CompanyName="test", CompanyCreditLimit="test",
                                    CreditLimitCurrency="test")


def test_CustomerCompanyInterface_create(interface: CustomerCompanyInterface):
    assert interface


def test_CustomerCompanyInterface_works(interface: CustomerCompanyInterface):
    customercompany = CustomerCompany(**interface)
    assert customercompany
