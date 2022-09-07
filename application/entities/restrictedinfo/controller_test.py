from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import RestrictedInfo
from .schema import RestrictedInfoSchema
from .service import RestrictedInfoService


def make_restrictedinfo(
        personid: int = 1, dateofbirth: str = "test", dateofdeath: str = "test", governmentid: str = "test",
        passportid: str = "test", hiredire: str = "test", senioritycode: int = 1
) -> RestrictedInfo:
    return RestrictedInfo(PersonId=personid, DateOfBirth=dateofbirth, DateOfDeath=dateofdeath,
                          GovernmentId=governmentid, PassportId=passportid, HireDire=hiredire,
                          SeniorityCode=senioritycode)


class TestRestrictedInfoResource:
    @patch.object(
        RestrictedInfoService,
        "get_all",
        lambda: [
            make_restrictedinfo(),
            make_restrictedinfo(PersonId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                RestrictedInfoSchema(many=True)
                    .dump(
                    [
                        make_restrictedinfo(),
                        make_restrictedinfo(PersonId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        RestrictedInfoService, "create", lambda create_request: RestrictedInfo(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(PersonId=1, DateOfBirth="test", DateOfDeath="test", GovernmentId="test", PassportId="test",
                           HireDire="test", SeniorityCode=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                RestrictedInfoSchema()
                    .dump(RestrictedInfo(PersonId=payload[1], DateOfBirth=payload["test"], DateOfDeath=payload["test"],
                                         GovernmentId=payload["test"], PassportId=payload["test"],
                                         HireDire=payload["test"], SeniorityCode=payload[1]))

            )
            assert result == expected


class TestRestrictedInfoIdResource:
    @patch.object(RestrictedInfoService, "get_by_id", lambda id: make_restrictedinfo(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_restrictedinfo(id=123)
            print(f"result = ", result)
            assert result["PersonId"] == expected.PersonId

    @patch.object(RestrictedInfoService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
