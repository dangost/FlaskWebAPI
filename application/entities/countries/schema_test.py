from pytest import fixture

from .model import Country
from .schema import CountrySchema
from .interface import CountryInterface


@fixture
def schema() -> CountrySchema:
    return CountrySchema()


def test_CountrySchema_create(schema: CountrySchema):
    assert schema


def test_CountrySchema_works(schema: CountrySchema):
    params: CountryInterface = schema.load(
        {"CountryName": "test", "CountryCode": "test", "NatLangCode": 1, "CurrencyCode": "test"}
    )
    country = Country(**params)

    assert country.CountryName == "test"
    assert country.CountryCode == "test"
    assert country.NatLangCode == 1
    assert country.CurrencyCode == "test"


