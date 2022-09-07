from mypy_extensions import TypedDict


class PersonLocationInterface(TypedDict, total=False):
    PersonsPersonId: int

    LocationsLocationsId: int

    SubAddress: str

    LocationUsage: str

    Notes: str
