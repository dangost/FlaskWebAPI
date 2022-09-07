from pytest import fixture

from .interface import CustomerInterface
from .model import Customer
from .schema import CustomerSchema


@fixture
def schema() -> CustomerSchema:
    return CustomerSchema()


def test_CustomerSchema_create(schema: CustomerSchema):
    assert schema


def test_CustomerSchema_works(schema: CustomerSchema):
    params: CustomerInterface = schema.load(
        {"CustomerId": 1, "PersonId": 1, "CustomEmployeeId": 1, "AccountMgrId": 1, "IncomeLevel": 1}
    )
    customer = Customer(**params)

    assert customer.CustomerId == 1
    assert customer.PersonId == 1
    assert customer.CustomEmployeeId == 1
    assert customer.AccountMgrId == 1
    assert customer.IncomeLevel == 1
