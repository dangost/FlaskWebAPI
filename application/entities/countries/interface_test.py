from pytest import fixture

from .interface import CountryInterface
from .model import Country


@fixture
def interface() -> CountryInterface:
    return CountryInterface(CountryId=1, CountryName="test", CountryCode="test", NatLangCode=1, CurrencyCode="test")


def test_CountryInterface_create(interface: CountryInterface):
    assert interface


def test_CountryInterface_works(interface: CountryInterface):
    country = Country(**interface)
    assert country
