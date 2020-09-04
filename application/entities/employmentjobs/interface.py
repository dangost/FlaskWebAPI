from mypy_extensions import TypedDict


class EmploymentJobsInterface(TypedDict, total=False):
    CountriesCountryId: int

    JobTitle: str

    MinSalary: int

    MaxSalary: int



