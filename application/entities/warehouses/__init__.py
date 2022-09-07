from .model import Warehouse  # noqa
from .schema import WarehouseSchema  # noqa

BASE_ROUTE = "Warehouses"


def register_routes(api, app, root="api"):
    from .controller import api as warehouses_api

    api.add_namespace(warehouses_api, path=f"/{root}/{BASE_ROUTE}")
