from .model import Customer  # noqa
from .schema import CustomerSchema  # noqa

BASE_ROUTE = "customer"


def register_routes(api, app, root="api"):
    from .controller import api as Customers_api

    api.add_namespace(customers_api, path=f"/{root}/{BASE_ROUTE}")

