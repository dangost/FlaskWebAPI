from .model import CustomerEmployee  # noqa
from .schema import CustomerEmployeeSchema  # noqa

BASE_ROUTE = "CustomerEmployees"


def register_routes(api, app, root="api"):
    from .controller import api as customeremployees_api

    api.add_namespace(customeremployees_api, path=f"/{root}/{BASE_ROUTE}")

