from pytest import fixture

from .interface import CustomerCompanyInterface
from .model import CustomerCompany
from .schema import CustomerCompanySchema


@fixture
def schema() -> CustomerCompanySchema:
    return CustomerCompanySchema()


def test_CustomerCompanySchema_create(schema: CustomerCompanySchema):
    assert schema


def test_CustomerCompanySchema_works(schema: CustomerCompanySchema):
    params: CustomerCompanyInterface = schema.load(
        {"CompanyName": "test", "CompanyCreditLimit": "test", "CreditLimitCurrency": "test"}
    )
    customercompany = CustomerCompany(**params)

    assert customercompany.CompanyName == "test"
    assert customercompany.CompanyCreditLimit == "test"
    assert customercompany.CreditLimitCurrency == "test"
