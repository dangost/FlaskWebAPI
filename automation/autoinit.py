class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "", "PhoneNumberId", "ProductId", "", "WarehouseId"]

base = [
    {"CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int",
     "CreditLimitCurrency": "int"},
    {"PersonId": "int", "HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string",
     "Salary": "string", "CommissionPercent": "int", "Employmentcol": "string"},
    {"CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvaileble": "int"},
    {"CountryId": "int", "AdressLine1": "string", "AdressLine2": "string", "City": "string", "State": "string",
     "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string",
     "ShippingNotes": "string", "CountriesCountryId": "int"},
    {"OrderId": "int", "ProductId": "int", "UnitPrice": "int", "Quantity": "int"},
    {"CustomerId": "int", "SalesRepId": "int", "OrderDate": "string", "OrderCode": "string", "OrderStatus": "string",
     "OrderTotal": "int", "OrderCurrency": "string", "PromotionCode": "string"},
    {"FirstName": "string", "LastName": "string", "MiddleName": "string", "Nickname": "string", "NatLangCode": "int",
     "CultureCode": "int", "Gender": "string"},
    {"LocationsLocationsId": "int", "SubAdress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PeoplePersonId": "int", "LocationLocationId": "int", "Phonenumber": "int", "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantlyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\FlaskWebAPI\application\entities"

import os
for i in range(len(class_names)):
    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        continue
    new_path = folder_path+"\\__init__.py"
    file = open(new_path, 'w')

    temp = '''from .model import '''+class_names[i]+'''  # noqa
from .schema import '''+class_names[i]+'''Schema  # noqa

BASE_ROUTE = "'''+class_names[i].lower()+'''"


def register_routes(api, app, root="api"):
    from .controller import api as '''+list_names[i]+'''_api

    api.add_namespace('''+list_names[i].lower()+'''_api, path=f"/{root}/{BASE_ROUTE}")

'''
    file.write(temp)