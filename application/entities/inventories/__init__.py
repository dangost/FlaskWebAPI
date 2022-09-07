from .model import Inventory  # noqa
from .schema import InventorySchema  # noqa

BASE_ROUTE = "Inventories"


def register_routes(api, app, root="api"):
    from .controller import api as inventories_api

    api.add_namespace(inventories_api, path=f"/{root}/{BASE_ROUTE}")
