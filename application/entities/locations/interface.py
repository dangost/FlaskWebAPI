from mypy_extensions import TypedDict


class LocationInterface(TypedDict, total=False):
    CountryId: int

    AdressLine1: str

    AdressLine2: str

    City: str

    State: str

    District: str

    PostalCode: str

    LocationTypeCode: int

    Description: str

    ShippingNotes: str

    CountriesCountryId: int



