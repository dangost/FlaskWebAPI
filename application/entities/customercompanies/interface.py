from mypy_extensions import TypedDict


class CustomerCompanyInterface(TypedDict, total=False):
    CompanyId: int

    CompanyName: str

    CompanyCreditLimit: str

    CreditLimitCurrency: str
