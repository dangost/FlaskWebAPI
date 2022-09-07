from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import PersonLocation
from .schema import PersonLocationSchema
from .service import PersonLocationsService


def make_personlocation(
        personspersonid: int = 1, locationslocationsid: int = 1, subaddress: str = "test", locationusage: str = "test",
        notes: str = "test"
) -> PersonLocation:
    return PersonLocation(PersonsPersonId=personspersonid, LocationsLocationsId=locationslocationsid,
                          SubAddress=subaddress, LocationUsage=locationusage, Notes=notes)


class TestPersonLocationResource:
    @patch.object(
        PersonLocationsService,
        "get_all",
        lambda: [
            make_personlocation(),
            make_personlocation(PeoplePersonId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                PersonLocationSchema(many=True)
                    .dump(
                    [
                        make_personlocation(),
                        make_personlocation(PeoplePersonId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        PersonLocationsService, "create", lambda create_request: PersonLocation(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(PeoplePersonId=1, LocationsLocationsId=1, SubAddress="test", LocationUsage="test",
                           Notes="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                PersonLocationSchema()
                    .dump(PersonLocation(PeoplePersonId=payload[1], LocationsLocationsId=payload[1],
                                         SubAddress=payload["test"], LocationUsage=payload["test"],
                                         Notes=payload["test"]))

            )
            assert result == expected


class TestPersonLocationIdResource:
    @patch.object(PersonLocationsService, "get_by_id", lambda id: make_personlocation(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_personlocation(id=123)
            print(f"result = ", result)
            assert result["PeoplePersonId"] == expected.PeoplePersonId

    @patch.object(PersonLocationsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
