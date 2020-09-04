from .model import Country  # noqa
from .schema import CountrySchema  # noqa

BASE_ROUTE = "Countries"


def register_routes(api, app, root="api"):
    from .controller import api as countries_api

    api.add_namespace(countries_api, path=f"/{root}/{BASE_ROUTE}")

