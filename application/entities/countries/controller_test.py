from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Country
from .schema import CountrySchema
from .service import CountriesService


def make_country(
        countryid: int = 1, countryname: str = "test", countrycode: str = "test", natlangcode: int = 1,
        currencycode: str = "test"
) -> Country:
    return Country(CountryId=countryid, CountryName=countryname, CountryCode=countrycode, NatLangCode=natlangcode,
                   CurrencyCode=currencycode)


class TestCountryResource:
    @patch.object(
        CountriesService,
        "get_all",
        lambda: [
            make_country(),
            make_country(CountryId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                CountrySchema(many=True)
                    .dump(
                    [
                        make_country(),
                        make_country(CountryId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        CountriesService, "create", lambda create_request: Country(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(CountryName="test", CountryCode="test", NatLangCode=1, CurrencyCode="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                CountrySchema()
                    .dump(Country(CountryName=payload["test"], CountryCode=payload["test"], NatLangCode=payload[1],
                                  CurrencyCode=payload["test"]))

            )
            assert result == expected


class TestCountryIdResource:
    @patch.object(CountriesService, "get_by_id", lambda id: make_country(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_country(id=123)
            print(f"result = ", result)
            assert result["CountryId"] == expected.CountryId

    @patch.object(CountriesService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
