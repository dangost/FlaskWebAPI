from mypy_extensions import TypedDict


class PersonLocationInterface(TypedDict, total=False):
    LocationsLocationsId: int

    SubAdress: str

    LocationUsage: str

    Notes: str



