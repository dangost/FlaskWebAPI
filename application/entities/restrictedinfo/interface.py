from mypy_extensions import TypedDict


class RestrictedInfoInterface(TypedDict, total=False):
    DateOfBirth: str

    DateOfDeath: str

    GovernmentId: str

    PassportId: str

    HireDire: str

    SeniorityCode: int



