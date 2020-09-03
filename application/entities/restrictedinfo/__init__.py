from .model import RestrictedInfo  # noqa
from .schema import RestrictedInfoSchema  # noqa

BASE_ROUTE = "restrictedinfo"


def register_routes(api, app, root="api"):
    from .controller import api as RestrictedInfo_api

    api.add_namespace(restrictedinfo_api, path=f"/{root}/{BASE_ROUTE}")

