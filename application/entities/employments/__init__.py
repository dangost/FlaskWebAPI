from .model import Employment  # noqa
from .schema import EmploymentSchema  # noqa

BASE_ROUTE = "Employments"


def register_routes(api, app, root="api"):
    from .controller import api as employments_api

    api.add_namespace(employments_api, path=f"/{root}/{BASE_ROUTE}")

