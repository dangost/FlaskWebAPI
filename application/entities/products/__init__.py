from .model import Product  # noqa
from .schema import ProductSchema  # noqa

BASE_ROUTE = "Products"


def register_routes(api, app, root="api"):
    from .controller import api as products_api

    api.add_namespace(products_api, path=f"/{root}/{BASE_ROUTE}")
