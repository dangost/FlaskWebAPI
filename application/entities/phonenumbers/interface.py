from mypy_extensions import TypedDict


class PhoneNumberInterface(TypedDict, total=False):
    PhoneNumberId: int

    PeoplePersonId: int

    LocationLocationId: int

    PhoneNumber: int

    CountryCode: int

    PhoneType: int
