from mypy_extensions import TypedDict


class CustomerInterface(TypedDict, total=False):
    PersonId: int

    CustomEmployeeId: int

    AccountMgrId: int

    IncomeLevel: int



