from .model import Product  # noqa
from .schema import ProductSchema  # noqa

BASE_ROUTE = "product"


def register_routes(api, app, root="api"):
    from .controller import api as Products_api

    api.add_namespace(products_api, path=f"/{root}/{BASE_ROUTE}")

