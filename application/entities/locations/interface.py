from mypy_extensions import TypedDict


class LocationInterface(TypedDict, total=False):
    LocationId: int

    CountryId: int

    AddressLine1: str

    AddressLine2: str

    City: str

    State: str

    District: str

    PostalCode: str

    LocationTypeCode: int

    Description: str

    ShippingNotes: str

    CountriesCountryId: int



