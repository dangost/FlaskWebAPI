from mypy_extensions import TypedDict


class EmploymentJobsInterface(TypedDict, total=False):
    HRJobId: int

    CountriesCountryId: int

    JobTitle: str

    MinSalary: int

    MaxSalary: int
