from pytest import fixture

from .interface import CustomerEmployeeInterface
from .model import CustomerEmployee
from .schema import CustomerEmployeeSchema


@fixture
def schema() -> CustomerEmployeeSchema:
    return CustomerEmployeeSchema()


def test_CustomerEmployeeSchema_create(schema: CustomerEmployeeSchema):
    assert schema


def test_CustomerEmployeeSchema_works(schema: CustomerEmployeeSchema):
    params: CustomerEmployeeInterface = schema.load(
        {"CompanyId": 1, "BadgeNumber": "test", "JobTitle": "test", "Department": "test", "CreditLimit": 1,
         "CreditLimitCurrency": 1}
    )
    customeremployee = CustomerEmployee(**params)

    assert customeremployee.CompanyId == 1
    assert customeremployee.BadgeNumber == "test"
    assert customeremployee.JobTitle == "test"
    assert customeremployee.Department == "test"
    assert customeremployee.CreditLimit == 1
    assert customeremployee.CreditLimitCurrency == 1
