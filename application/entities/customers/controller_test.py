from unittest.mock import patch
from flask.testing import FlaskClient
from .service import CustomersService
from .schema import CustomerSchema
from .model import Customer
from . import BASE_ROUTE


def make_customer(
    customerid: int = 1, personid: int = 1, customemployeeid: int = 1, accountmgrid: int = 1, incomelevel: int = 1
) -> Customer:
    return Customer(CustomerId=customerid, PersonId=personid, CustomEmployeeId=customemployeeid, AccountMgrId=accountmgrid, IncomeLevel=incomelevel)


class TestCustomerResource:
    @patch.object(
        CustomersService,
        "get_all",
        lambda: [
            make_customer(),
            make_customer(CustomerId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                CustomerSchema(many=True)
                .dump(
                    [
                        make_customer(),
                        make_customer(CustomerId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        CustomersService, "create", lambda create_request: Customer(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(CustomerId=1, PersonId=1, CustomEmployeeId=1, AccountMgrId=1, IncomeLevel=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                CustomerSchema()
                .dump(Customer(CustomerId=payload[1], PersonId=payload[1], CustomEmployeeId=payload[1], AccountMgrId=payload[1], IncomeLevel=payload[1]))

            )
            assert result == expected


class TestCustomerIdResource:
    @patch.object(CustomersService, "get_by_id", lambda id: make_customer(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_customer(id=123)
            print(f"result = ", result)
            assert result["CustomerId"] == expected.CustomerId

    @patch.object(CustomersService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

