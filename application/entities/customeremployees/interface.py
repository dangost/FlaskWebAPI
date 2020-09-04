from mypy_extensions import TypedDict


class CustomerEmployeeInterface(TypedDict, total=False):
    CustomerEmployeeId: int

    CompanyId: int

    BadgeNumber: str

    JobTitle: str

    Department: str

    CreditLimit: int

    CreditLimitCurrency: int



