class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "PeoplePersonId", "PhoneNumberId", "ProductId", "PersonId", "WarehouseId"]
base_with_id = [
    {"CountryId": "int", "CountryName": "string", "CountryCode": "string", "NatLangCode": "int",
     "CurrencyCode": "string"},
    {"CustomerId": "int", "PersonId": "int", "CustomEmployeeId": "int", "AccountMgrId": "int", "IncomeLevel": "int"},
    {"CompanyId": "int", "CompanyName": "string", "CompanyCreditLimit": "string", "CreditLimitCurrency": "string"},
    {"CustomerEmployeeId": "int", "CompanyId": "int", "BadgeNumber": "string", "JobTitle": "string",
     "Department": "string", "CreditLimit": "int",
     "CreditLimitCurrency": "int"},
    {"EmployeeId": "int", "PersonId": "int", "HRJobId": "int", "ManagerEmployeeId": "int", "StartDate": "string",
     "EndDate": "string",
     "Salary": "string", "CommissionPercent": "int", "EmploymentCol": "string"},
    {"HRJobId": "int", "CountriesCountryId": "int", "JobTitle": "string", "MinSalary": "int", "MaxSalary": "int"},
    {"InventoryId": "int", "ProductId": "int", "WarehouseId": "int", "QuantityOnHand": "int",
     "QuantityAvailable": "int"},
    {"LocationId": "int", "CountryId": "int", "AddressLine1": "string", "AddressLine2": "string", "City": "string",
     "State": "string",
     "District": "string", "PostalCode": "string", "LocationTypeCode": "int", "Description": "string",
     "ShippingNotes": "string", "CountriesCountryId": "int"},
    {"OrderItemId": "int", "OrderId": "int", "ProductId": "int", "UnitPrice": "int", "Quantity": "int"},
    {"OrderId": "int", "CustomerId": "int", "SalesRepId": "int", "OrderDate": "string", "OrderCode": "string",
     "OrderStatus": "string",
     "OrderTotal": "int", "OrderCurrency": "string", "PromotionCode": "string"},
    {"PersonId": "int", "FirstName": "string", "LastName": "string", "MiddleName": "string", "Nickname": "string",
     "NatLangCode": "int",
     "CultureCode": "int", "Gender": "string"},
    {"PersonsPersonId": "int", "LocationsLocationsId": "int", "SubAddress": "string", "LocationUsage": "string",
     "Notes": "string"},
    {"PhoneNumberId": "int", "PeoplePersonId": "int", "LocationLocationId": "int", "PhoneNumber": "int",
     "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductId": "int", "ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"PersonId": "int", "DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string",
     "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"WarehouseId": "int", "LocationId": "int", "WarehouseName": "string"}
]



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
    {"PeoplePersonId": "int", "LocationsLocationsId": "int", "SubAddress": "string", "LocationUsage": "string", "Notes": "string"},
    {"PeoplePersonId": "int", "LocationLocationId": "int", "PhoneNumber": "int", "CountryCode": "int",
     "PhoneType": "int"},
    {"ProductName": "string", "Description": "string", "Category": "int", "WeightClass": "string",
     "WarrantyPeriod": "int", "SupplierId": "int", "Status": "string", "ListPrice": "int", "MinimumPrice": "int",
     "PriceCurrency": "string", "CatalogURL": "string"},
    {"PersonId": "int", "DateOfBirth": "string", "DateOfDeath": "string", "GovernmentId": "string", "PassportId": "string",
     "HireDire": "string", "SeniorityCode": "int"},
    {"WarehouseId": "int", "LocationId": "int", "WarehouseName": "string"}
]

path = r"D:\Projects\Regula\Web\FlaskWebAPI\application\entities"

import os
for i in range(len(class_names)):
    '''widget_id=1, name="Yin", purpose="thing 1"'''
    t = ""
    t1 = ""
    var1 = ""
    for each in base_with_id[i]:
        if base_with_id[i].get(each) == "int":
            var1 = "=16, "
        else:
            var1 = "=\"test16\", "
        t += each+var1

    for each in base_with_id[i]:
        if base_with_id[i].get(each) == "int":
            var1 = "=1, "
        else:
            var = "=\"test\", "
        t1 += each+var1
        pass
    t12 = ""
    for each in base[i]:
        if base[i].get(each) == "int":
            var1 = "=1, "
        else:
            var1 = "=\"test\", "
        t12 += each+var1
        break
        pass


    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path+"\\service_test.py"
    file = open(new_path, 'w')

    '''(CountryName=new_attrs["CountryName"], ... )'''

    temp = '''from flask_sqlalchemy import SQLAlchemy
from typing import List
from .model import '''+class_names[i]+'''
from .service import '''+list_names[i]+'''Service  # noqa
from .interface import '''+class_names[i]+'''Interface


def test_get_all(db: SQLAlchemy):  # noqa
    yin: '''+class_names[i]+''' = '''+class_names[i]+'''('''+t[0:-2]+''')
    yang: '''+class_names[i]+''' = '''+class_names[i]+'''('''+t[0:-2]+''')
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    results: List['''+class_names[i]+'''] = '''+list_names[i]+'''Service.get_all()

    assert len(results) == 2
    assert yin in results and yang in results


def test_delete_by_id(db: SQLAlchemy):  # noqa
    yin: '''+class_names[i]+''' = '''+class_names[i]+'''('''+t[0:-2]+''')
    yang: '''+class_names[i]+''' = '''+class_names[i]+'''('''+t[0:-2]+''')
    db.session.add(yin)
    db.session.add(yang)
    db.session.commit()

    '''+list_names[i]+'''Service.delete_by_id(1)
    db.session.commit()

    results: List['''+class_names[i]+'''] = '''+class_names[i]+'''.query.all()

    assert len(results) == 1
    assert yin not in results and yang in results


def test_create(db: SQLAlchemy):  # noqa

    yin: '''+class_names[i]+'''Interface = dict('''+t12[0:-2]+''')
    '''+list_names[i]+'''Service.create(yin)
    results: List['''+class_names[i]+'''] = '''+class_names[i]+'''.query.all()

    assert len(results) == 1

    for k in yin.keys():
        assert getattr(results[0], k) == yin[k]


'''
    file.write(temp)