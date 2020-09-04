from .model import CustomerCompany  # noqa
from .schema import CustomerCompanySchema  # noqa

BASE_ROUTE = "CustomerCompanies"


def register_routes(api, app, root="api"):
    from .controller import api as customercompanies_api

    api.add_namespace(customercompanies_api, path=f"/{root}/{BASE_ROUTE}")

