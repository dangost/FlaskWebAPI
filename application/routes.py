def register_routes(api, app, root="api"):
    from application.entities.countries import register_routes as attach_countries

    # Add routes
    attach_countries(api, api)
