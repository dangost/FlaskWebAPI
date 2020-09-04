from mypy_extensions import TypedDict


class CustomerCompanyInterface(TypedDict, total=False):
    CompanyName: str

    CompanyCreditLimit: str

    CreditLimitCurrency: str



