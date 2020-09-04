from mypy_extensions import TypedDict


class EmploymentInterface(TypedDict, total=False):
    EmployeeId: int

    PersonId: int

    HRJobId: int

    ManagerEmployeeId: int

    StartDate: str

    EndDate: str

    Salary: str

    CommissionPercent: int

    EmploymentCol: str



