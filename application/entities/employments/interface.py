from mypy_extensions import TypedDict


class EmploymentInterface(TypedDict, total=False):
    PersonId: int

    HRJobId: int

    ManagerEmployeeId: int

    StartDate: str

    EndDate: str

    Salary: str

    CommissionPercent: int

    Employmentcol: str



