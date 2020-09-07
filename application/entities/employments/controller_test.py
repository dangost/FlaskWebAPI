from unittest.mock import patch
from flask.testing import FlaskClient
from .service import EmploymentsService
from .schema import EmploymentSchema
from .model import Employment
from . import BASE_ROUTE


def make_employment(
    employeeid: int = 1, personid: int = 1, hrjobid: int = 1, manageremployeeid: int = 1, startdate:str = "test", enddate:str = "test", salary:str = "test", commissionpercent: int = 1, employmentcol:str = "test"
) -> Employment:
    return Employment(EmployeeId=employeeid, PersonId=personid, HRJobId=hrjobid, ManagerEmployeeId=manageremployeeid, StartDate=startdate, EndDate=enddate, Salary=salary, CommissionPercent=commissionpercent, EmploymentCol=employmentcol)


class TestEmploymentResource:
    @patch.object(
        EmploymentsService,
        "get_all",
        lambda: [
            make_employment(),
            make_employment(EmployeeID=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                EmploymentSchema(many=True)
                .dump(
                    [
                        make_employment(),
                        make_employment(EmployeeID=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        EmploymentsService, "create", lambda create_request: Employment(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(PersonId=1, HRJobId=1, ManagerEmployeeId=1, StartDate="test", EndDate="test", Salary="test", CommissionPercent=1, EmploymentCol="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                EmploymentSchema()
                .dump(Employment(PersonId=payload[1], HRJobId=payload[1], ManagerEmployeeId=payload[1], StartDate=payload["test"], EndDate=payload["test"], Salary=payload["test"], CommissionPercent=payload[1], EmploymentCol=payload["test"]))

            )
            assert result == expected


class TestEmploymentIdResource:
    @patch.object(EmploymentsService, "get_by_id", lambda id: make_employment(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_employment(id=123)
            print(f"result = ", result)
            assert result["EmployeeID"] == expected.EmployeeID

    @patch.object(EmploymentsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

