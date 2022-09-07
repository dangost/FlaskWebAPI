from .model import Location  # noqa
from .schema import LocationSchema  # noqa

BASE_ROUTE = "Locations"


def register_routes(api, app, root="api"):
    from .controller import api as locations_api

    api.add_namespace(locations_api, path=f"/{root}/{BASE_ROUTE}")
