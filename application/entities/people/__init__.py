from .model import Person  # noqa
from .schema import PersonSchema  # noqa

BASE_ROUTE = "People"


def register_routes(api, app, root="api"):
    from .controller import api as people_api

    api.add_namespace(people_api, path=f"/{root}/{BASE_ROUTE}")
