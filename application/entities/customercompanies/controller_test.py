from unittest.mock import patch
from flask.testing import FlaskClient
from .service import CustomerCompaniesService
from .schema import CustomerCompanySchema
from .model import CustomerCompany
from . import BASE_ROUTE


def make_customercompany(
    companyid: int = 1, companyname:str = "test", companycreditlimit:str = "test", creditlimitcurrency:str = "test"
) -> CustomerCompany:
    return CustomerCompany(CompanyId=companyid, CompanyName=companyname, CompanyCreditLimit=companycreditlimit, CreditLimitCurrency=creditlimitcurrency)


class TestCustomerCompanyResource:
    @patch.object(
        CustomerCompaniesService,
        "get_all",
        lambda: [
            make_customercompany(),
            make_customercompany(CompanyId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                CustomerCompanySchema(many=True)
                .dump(
                    [
                        make_customercompany(),
                        make_customercompany(CompanyId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        CustomerCompaniesService, "create", lambda create_request: CustomerCompany(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(CompanyName="test", CompanyCreditLimit="test", CreditLimitCurrency="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                CustomerCompanySchema()
                .dump(CustomerCompany(CompanyName=payload["test"], CompanyCreditLimit=payload["test"], CreditLimitCurrency=payload["test"]))

            )
            assert result == expected


class TestCustomerCompanyIdResource:
    @patch.object(CustomerCompaniesService, "get_by_id", lambda id: make_customercompany(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_customercompany(id=123)
            print(f"result = ", result)
            assert result["CompanyId"] == expected.CompanyId

    @patch.object(CustomerCompaniesService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

