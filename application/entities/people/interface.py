from mypy_extensions import TypedDict


class PersonInterface(TypedDict, total=False):
    PersonId: int

    FirstName: str

    LastName: str

    MiddleName: str

    Nickname: str

    NatLangCode: int

    CultureCode: int

    Gender: str



