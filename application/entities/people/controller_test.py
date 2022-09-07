from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Person
from .schema import PersonSchema
from .service import PeopleService


def make_person(
        personid: int = 1, firstname: str = "test", lastname: str = "test", middlename: str = "test",
        nickname: str = "test", natlangcode: int = 1, culturecode: int = 1, gender: str = "test"
) -> Person:
    return Person(PersonId=personid, FirstName=firstname, LastName=lastname, MiddleName=middlename, Nickname=nickname,
                  NatLangCode=natlangcode, CultureCode=culturecode, Gender=gender)


class TestPersonResource:
    @patch.object(
        PeopleService,
        "get_all",
        lambda: [
            make_person(),
            make_person(Id=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                PersonSchema(many=True)
                    .dump(
                    [
                        make_person(),
                        make_person(Id=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        PeopleService, "create", lambda create_request: Person(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(FirstName="test", LastName="test", MiddleName="test", Nickname="test", NatLangCode=1,
                           CultureCode=1, Gender="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                PersonSchema()
                    .dump(Person(FirstName=payload["test"], LastName=payload["test"], MiddleName=payload["test"],
                                 Nickname=payload["test"], NatLangCode=payload[1], CultureCode=payload[1],
                                 Gender=payload["test"]))

            )
            assert result == expected


class TestPersonIdResource:
    @patch.object(PeopleService, "get_by_id", lambda id: make_person(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_person(id=123)
            print(f"result = ", result)
            assert result["Id"] == expected.Id

    @patch.object(PeopleService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
