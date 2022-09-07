class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "PeoplePersonId", "PhoneNumberId", "ProductId", "PersonId",
            "WarehouseId"]
base = [
    {"CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"CustomerId": "int", "PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int",
     "CreditLimitCurrency": "int"},
    {"PersonId": "int", "HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string",
     "Salary": "string", "CommissionPercent": "int", "EmploymentCol": "string"},
    {"CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvailable": "int"},
    {"CountryId": "int", "AddressLine1": "string", "AddressLine2": "string", "City": "string", "State": "string",
     "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string",
     "ShippingNotes": "string", "CountriesCountryId": "int"},
    {"OrderId": "int", "ProductId": "int", "UnitPrice": "int", "Quantity": "int"},
    {"CustomerId": "int", "SalesRepId": "int", "OrderDate": "string", "OrderCode": "string", "OrderStatus": "string",
     "OrderTotal": "int", "OrderCurrency": "string", "PromotionCode": "string"},
    {"FirstName": "string", "LastName": "string", "MiddleName": "string", "Nickname": "string", "NatLangCode": "int",
     "CultureCode": "int", "Gender": "string"},
    {"PeoplePersonId": "int", "LocationsLocationsId": "int", "SubAddress": "string", "LocationUsage": "string",
     "Notes": "string"},
    {"PeoplePersonId": "int", "LocationLocationId": "int", "PhoneNumber": "int", "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"PersonId": "int", "DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string",
     "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"WarehouseId": "int", "LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\FlaskWebAPI\application\entities"

import os

for i in range(len(class_names)):

    t = ""
    asse = ""
    for each in base[i]:

        ans = "1"
        if base[i].get(each) == "int":
            ans = "1"
        else:
            ans = "\"test\""
        asse += "    assert " + class_names[i].lower() + "." + each + " == " + ans + "\n"

        var = ""
        if base[i].get(each) == "int":
            var = "1"
        else:
            var = "\"test\""
        '''widget_id=1, name="Test widget", purpose="Test purpose"'''
        t += "\"" + each + "\": " + var + ", "

    '''CountryName = fields.String(attribute="CountryName")'''
    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path + "\\schema_test.py"
    file = open(new_path, 'w')

    temp = '''from pytest import fixture

from .model import ''' + class_names[i] + '''
from .schema import ''' + class_names[i] + '''Schema
from .interface import ''' + class_names[i] + '''Interface


@fixture
def schema() -> ''' + class_names[i] + '''Schema:
    return ''' + class_names[i] + '''Schema()


def test_''' + class_names[i] + '''Schema_create(schema: ''' + class_names[i] + '''Schema):
    assert schema


def test_''' + class_names[i] + '''Schema_works(schema: ''' + class_names[i] + '''Schema):
    params: ''' + class_names[i] + '''Interface = schema.load(
        {''' + t[0:-2] + '''}
    )
    ''' + class_names[i].lower() + ''' = ''' + class_names[i] + '''(**params)

''' + asse + '''

'''
    file.write(temp)
