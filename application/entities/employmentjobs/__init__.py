from .model import EmploymentJobs  # noqa
from .schema import EmploymentJobsSchema  # noqa

BASE_ROUTE = "EmploymentJobs"


def register_routes(api, app, root="api"):
    from .controller import api as employmentjobs_api

    api.add_namespace(employmentjobs_api, path=f"/{root}/{BASE_ROUTE}")
