from unittest.mock import patch
from flask.testing import FlaskClient
from .service import PhoneNumbersService
from .schema import PhoneNumberSchema
from .model import PhoneNumber
from . import BASE_ROUTE


def make_phonenumber(
    phonenumberid: int = 1, peoplepersonid: int = 1, locationlocationid: int = 1, phonenumber: int = 1, countrycode: int = 1, phonetype: int = 1
) -> PhoneNumber:
    return PhoneNumber(PhoneNumberId=phonenumberid, PeoplePersonId=peoplepersonid, LocationLocationId=locationlocationid, PhoneNumber=phonenumber, CountryCode=countrycode, PhoneType=phonetype)


class TestPhoneNumberResource:
    @patch.object(
        PhoneNumbersService,
        "get_all",
        lambda: [
            make_phonenumber(),
            make_phonenumber(PhoneNumberId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                PhoneNumberSchema(many=True)
                .dump(
                    [
                        make_phonenumber(),
                        make_phonenumber(PhoneNumberId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        PhoneNumbersService, "create", lambda create_request: PhoneNumber(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(PeoplePersonId=1, LocationLocationId=1, PhoneNumber=1, CountryCode=1, PhoneType=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                PhoneNumberSchema()
                .dump(PhoneNumber(PeoplePersonId=payload[1], LocationLocationId=payload[1], PhoneNumber=payload[1], CountryCode=payload[1], PhoneType=payload[1]))

            )
            assert result == expected


class TestPhoneNumberIdResource:
    @patch.object(PhoneNumbersService, "get_by_id", lambda id: make_phonenumber(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_phonenumber(id=123)
            print(f"result = ", result)
            assert result["PhoneNumberId"] == expected.PhoneNumberId

    @patch.object(PhoneNumbersService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

