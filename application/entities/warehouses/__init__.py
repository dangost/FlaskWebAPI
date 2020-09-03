from .model import Warehouse  # noqa
from .schema import WarehouseSchema  # noqa

BASE_ROUTE = "warehouse"


def register_routes(api, app, root="api"):
    from .controller import api as Warehouses_api

    api.add_namespace(warehouses_api, path=f"/{root}/{BASE_ROUTE}")

