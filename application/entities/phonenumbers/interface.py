from mypy_extensions import TypedDict


class PhoneNumberInterface(TypedDict, total=False):
    PeoplePersonId: int

    LocationLocationId: int

    Phonenumber: int

    CountryCode: int

    PhoneType: int



