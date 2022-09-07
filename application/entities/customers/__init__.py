from .model import Customer  # noqa
from .schema import CustomerSchema  # noqa

BASE_ROUTE = "Customers"


def register_routes(api, app, root="api"):
    from .controller import api as customers_api

    api.add_namespace(customers_api, path=f"/{root}/{BASE_ROUTE}")
