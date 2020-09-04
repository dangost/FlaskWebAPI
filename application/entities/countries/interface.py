from mypy_extensions import TypedDict


class CountryInterface(TypedDict, total=False):
    CountryName: str

    CountryCode: str

    NatLangCode: int

    CurrencyCode: str



