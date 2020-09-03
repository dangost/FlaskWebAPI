from .model import OrderItem  # noqa
from .schema import OrderItemSchema  # noqa

BASE_ROUTE = "orderitem"


def register_routes(api, app, root="api"):
    from .controller import api as OrderItems_api

    api.add_namespace(orderitems_api, path=f"/{root}/{BASE_ROUTE}")

