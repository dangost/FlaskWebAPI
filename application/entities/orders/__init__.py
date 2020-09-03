from .model import Orders  # noqa
from .schema import OrdersSchema  # noqa

BASE_ROUTE = "orders"


def register_routes(api, app, root="api"):
    from .controller import api as Orders_api

    api.add_namespace(orders_api, path=f"/{root}/{BASE_ROUTE}")

