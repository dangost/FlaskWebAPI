from .model import Inventory  # noqa
from .schema import InventorySchema  # noqa

BASE_ROUTE = "inventory"


def register_routes(api, app, root="api"):
    from .controller import api as Inventories_api

    api.add_namespace(inventories_api, path=f"/{root}/{BASE_ROUTE}")

