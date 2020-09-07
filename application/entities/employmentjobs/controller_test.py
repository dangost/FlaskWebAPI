from unittest.mock import patch
from flask.testing import FlaskClient
from .service import EmploymentJobsService
from .schema import EmploymentJobsSchema
from .model import EmploymentJobs
from . import BASE_ROUTE


def make_employmentjobs(
    hrjobid: int = 1, countriescountryid: int = 1, jobtitle:str = "test", minsalary: int = 1, maxsalary: int = 1
) -> EmploymentJobs:
    return EmploymentJobs(HRJobId=hrjobid, CountriesCountryId=countriescountryid, JobTitle=jobtitle, MinSalary=minsalary, MaxSalary=maxsalary)


class TestEmploymentJobsResource:
    @patch.object(
        EmploymentJobsService,
        "get_all",
        lambda: [
            make_employmentjobs(),
            make_employmentjobs(HRJobId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                EmploymentJobsSchema(many=True)
                .dump(
                    [
                        make_employmentjobs(),
                        make_employmentjobs(HRJobId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        EmploymentJobsService, "create", lambda create_request: EmploymentJobs(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(CountriesCountryId=1, JobTitle="test", MinSalary=1, MaxSalary=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                EmploymentJobsSchema()
                .dump(EmploymentJobs(CountriesCountryId=payload[1], JobTitle=payload["test"], MinSalary=payload[1], MaxSalary=payload[1]))

            )
            assert result == expected


class TestEmploymentJobsIdResource:
    @patch.object(EmploymentJobsService, "get_by_id", lambda id: make_employmentjobs(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_employmentjobs(id=123)
            print(f"result = ", result)
            assert result["HRJobId"] == expected.HRJobId

    @patch.object(EmploymentJobsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

