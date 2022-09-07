from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import CustomerEmployee
from .schema import CustomerEmployeeSchema
from .service import CustomerEmployeesService


def make_customeremployee(
        customeremployeeid: int = 1, companyid: int = 1, badgenumber: str = "test", jobtitle: str = "test",
        department: str = "test", creditlimit: int = 1, creditlimitcurrency: int = 1
) -> CustomerEmployee:
    return CustomerEmployee(CustomerEmployeeId=customeremployeeid, CompanyId=companyid, BadgeNumber=badgenumber,
                            JobTitle=jobtitle, Department=department, CreditLimit=creditlimit,
                            CreditLimitCurrency=creditlimitcurrency)


class TestCustomerEmployeeResource:
    @patch.object(
        CustomerEmployeesService,
        "get_all",
        lambda: [
            make_customeremployee(),
            make_customeremployee(CustomerEmployeeId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                CustomerEmployeeSchema(many=True)
                    .dump(
                    [
                        make_customeremployee(),
                        make_customeremployee(CustomerEmployeeId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        CustomerEmployeesService, "create", lambda create_request: CustomerEmployee(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(CompanyId=1, BadgeNumber="test", JobTitle="test", Department="test", CreditLimit=1,
                           CreditLimitCurrency=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                CustomerEmployeeSchema()
                    .dump(CustomerEmployee(CompanyId=payload[1], BadgeNumber=payload["test"], JobTitle=payload["test"],
                                           Department=payload["test"], CreditLimit=payload[1],
                                           CreditLimitCurrency=payload[1]))

            )
            assert result == expected


class TestCustomerEmployeeIdResource:
    @patch.object(CustomerEmployeesService, "get_by_id", lambda id: make_customeremployee(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_customeremployee(id=123)
            print(f"result = ", result)
            assert result["CustomerEmployeeId"] == expected.CustomerEmployeeId

    @patch.object(CustomerEmployeesService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
