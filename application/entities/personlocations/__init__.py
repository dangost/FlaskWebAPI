from .model import PersonLocation  # noqa
from .schema import PersonLocationSchema  # noqa

BASE_ROUTE = "personlocation"


def register_routes(api, app, root="api"):
    from .controller import api as PersonLocations_api

    api.add_namespace(personlocations_api, path=f"/{root}/{BASE_ROUTE}")

