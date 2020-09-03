from .model import Location  # noqa
from .schema import LocationSchema  # noqa

BASE_ROUTE = "location"


def register_routes(api, app, root="api"):
    from .controller import api as Locations_api

    api.add_namespace(locations_api, path=f"/{root}/{BASE_ROUTE}")

