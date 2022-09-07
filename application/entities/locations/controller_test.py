from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Location
from .schema import LocationSchema
from .service import LocationsService


def make_location(
        locationid: int = 1, countryid: int = 1, addressline1: str = "test", addressline2: str = "test",
        city: str = "test", state: str = "test", district: str = "test", postalcode: str = "test",
        locationtypecode: int = 1, description: str = "test", shippingnotes: str = "test", countriescountryid: int = 1
) -> Location:
    return Location(LocationId=locationid, CountryId=countryid, AddressLine1=addressline1, AddressLine2=addressline2,
                    City=city, State=state, District=district, PostalCode=postalcode, LocationTypeCode=locationtypecode,
                    Description=description, ShippingNotes=shippingnotes, CountriesCountryId=countriescountryid)


class TestLocationResource:
    @patch.object(
        LocationsService,
        "get_all",
        lambda: [
            make_location(),
            make_location(LocationId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                LocationSchema(many=True)
                    .dump(
                    [
                        make_location(),
                        make_location(LocationId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        LocationsService, "create", lambda create_request: Location(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(CountryId=1, AddressLine1="test", AddressLine2="test", City="test", State="test",
                           District="test", PostalCode="test", LocationTypeCode=1, Description="test",
                           ShippingNotes="test", CountriesCountryId=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                LocationSchema()
                    .dump(Location(CountryId=payload[1], AddressLine1=payload["test"], AddressLine2=payload["test"],
                                   City=payload["test"], State=payload["test"], District=payload["test"],
                                   PostalCode=payload["test"], LocationTypeCode=payload[1], Description=payload["test"],
                                   ShippingNotes=payload["test"], CountriesCountryId=payload[1]))

            )
            assert result == expected


class TestLocationIdResource:
    @patch.object(LocationsService, "get_by_id", lambda id: make_location(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_location(id=123)
            print(f"result = ", result)
            assert result["LocationId"] == expected.LocationId

    @patch.object(LocationsService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
