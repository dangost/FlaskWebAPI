from mypy_extensions import TypedDict


class RestrictedInfoInterface(TypedDict, total=False):
    PersonId: int

    DateOfBirth: str

    DateOfDeath: str

    GovernmentId: str

    PassportId: str

    HireDire: str

    SeniorityCode: int
