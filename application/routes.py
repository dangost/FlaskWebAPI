def register_routes(api, app, root="api"):
    from application.entities.countries import register_routes as attach_countries
    from application.entities.customers import register_routes as attach_customers
    from application.entities.customercompanies import register_routes as attach_customercompanies
    from application.entities.customeremployees import register_routes as attach_customeremployees
    from application.entities.employments import register_routes as attach_employments
    from application.entities.employmentjobs import register_routes as attach_employmentjobs
    from application.entities.inventories import register_routes as attach_inventories
    from application.entities.locations import register_routes as attach_locations
    from application.entities.orderitems import register_routes as attach_orderitems
    from application.entities.orders import register_routes as attach_orders
    from application.entities.people import register_routes as attach_people
    from application.entities.personlocations import register_routes as attach_personlocations
    from application.entities.phonenumbers import register_routes as attach_phonenumbers
    from application.entities.products import register_routes as attach_products
    from application.entities.restrictedinfo import register_routes as attach_restrictedinfo
    from application.entities.warehouses import register_routes as attach_warehouses

    #add routes
    attach_countries(api, api)
    attach_customers(api, api)
    attach_customercompanies(api, api)
    attach_customeremployees(api, api)
    attach_employments(api, api)
    attach_employmentjobs(api, api)
    attach_inventories(api, api)
    attach_locations(api, api)
    attach_orderitems(api, api)
    attach_orders(api, api)
    attach_people(api, api)
    attach_personlocations(api, api)
    attach_phonenumbers(api, api)
    attach_products(api, api)
    attach_restrictedinfo(api, api)
    attach_warehouses(api, api)

