from mypy_extensions import TypedDict


class CustomerEmployeeInterface(TypedDict, total=False):
    CompanyId: int

    BadgeNumber: str

    JobTitle: str

    Department: str

    CreditLimit: int

    CreditLimitCurrency: int



