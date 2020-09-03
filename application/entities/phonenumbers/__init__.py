from .model import PhoneNumber  # noqa
from .schema import PhoneNumberSchema  # noqa

BASE_ROUTE = "phonenumber"


def register_routes(api, app, root="api"):
    from .controller import api as PhoneNumbers_api

    api.add_namespace(phonenumbers_api, path=f"/{root}/{BASE_ROUTE}")

