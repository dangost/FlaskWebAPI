class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "PeoplePersonId", "PhoneNumberId", "ProductId", "PersonId", "WarehouseId"]
base = [
    {"CountryId": "int", "CountryName": "string", "CountryCode": "string", "NatLangCode": "int", "CurrencyCode": "string"},
    {"CustomerId": "int", "PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyId": "int", "CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CustomerEmployeeId": "int", "CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string", "Department": "string", "CreditLimit": "int",
     "CreditLimitCurrency": "int"},
    {"EmployeeId": "int", "PersonId": "int", "HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string", "EndDate": "string",
     "Salary": "string", "CommissionPercent": "int", "EmploymentCol": "string"},
    {"HRJobId": "int", "CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"InventoryId": "int", "ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int", "QuantityAvailable": "int"},
    {"LocationId": "int", "CountryId": "int", "AddressLine1": "string", "AddressLine2": "string", "City": "string", "State": "string",
     "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string",
     "ShippingNotes": "string", "CountriesCountryId": "int"},
    {"OrderItemId": "int", "OrderId": "int", "ProductId": "int", "UnitPrice": "int", "Quantity": "int"},
    {"OrderId": "int", "CustomerId": "int", "SalesRepId": "int", "OrderDate": "string", "OrderCode": "string", "OrderStatus": "string",
     "OrderTotal": "int", "OrderCurrency": "string", "PromotionCode": "string"},
    {"PersonId": "int", "FirstName": "string", "LastName": "string", "MiddleName": "string", "Nickname": "string", "NatLangCode": "int",
     "CultureCode": "int", "Gender": "string"},
    {"PersonsPersonId": "int", "LocationsLocationsId": "int", "SubAddress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PhoneNumberId": "int", "PeoplePersonId": "int", "LocationLocationId": "int", "PhoneNumber": "int", "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductId": "int", "ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"PersonId": "int", "DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"WarehouseId": "int", "LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\FlaskWebAPI\application\entities"

import os
for i in range(len(class_names)):

    t = ""
    for each in base[i]:
        var = ""
        if base[i].get(each) == "int":
            var = "1"
        else:
            var = "\"test\""
        '''widget_id=1, name="Test widget", purpose="Test purpose"'''
        t += each + "=" + var + ", "

    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path+"\\model_test.py"
    file = open(new_path, 'w')

    temp = '''from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from application.test.fixtures import app, db  # noqa
from .model import '''+class_names[i]+'''


@fixture
def '''+class_names[i].lower()+'''() -> '''+class_names[i]+''':
    return '''+class_names[i]+'''('''+t[0:-2]+''')


def test_'''+class_names[i]+'''_create('''+class_names[i].lower()+''': '''+class_names[i]+'''):
    assert '''+class_names[i].lower()+'''


def test_'''+class_names[i]+'''_retrieve('''+class_names[i].lower()+''': '''+class_names[i]+''', db: SQLAlchemy):  # noqa
    db.session.add('''+class_names[i].lower()+''')
    db.session.commit()
    s = '''+class_names[i]+'''.query.first()
    assert s.__dict__ == '''+class_names[i].lower()+'''.__dict__

'''
    file.write(temp)