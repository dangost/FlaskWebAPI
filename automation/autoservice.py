class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "PeoplePersonId", "PhoneNumberId", "ProductId", "PersonId", "WarehouseId"]
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

    t = ""
    for each in base[i]:

        t += " "+each+"=new_attrs[\""+each+"\"], "


    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path+"\\service.py"
    file = open(new_path, 'w')

    '''(CountryName=new_attrs["CountryName"], ... )'''

    temp = '''from application import db
from typing import List
from .model import '''+class_names[i]+'''
from .interface import '''+class_names[i]+'''Interface


class '''+list_names[i]+'''Service:
    @staticmethod
    def get_all() -> List['''+class_names[i]+''']:
        return '''+class_names[i]+'''.query.all()

    @staticmethod
    def get_by_id('''+class_names[i].lower()+'''_id: int) -> '''+class_names[i]+''':
        return '''+class_names[i]+'''.query.get('''+class_names[i].lower()+'''_id)

    @staticmethod
    def update('''+class_names[i].lower()+''': '''+class_names[i]+''', '''+class_names[i].lower()+'''_change_updates: '''+class_names[i]+'''Interface) -> '''+class_names[i]+''':
        '''+class_names[i].lower()+'''.update('''+class_names[i].lower()+'''_change_updates)
        db.session.commit()
        return '''+class_names[i].lower()+'''

    @staticmethod
    def delete_by_id('''+class_names[i].lower()+'''_id: int) -> List[int]:
        '''+class_names[i].lower()+''' = '''+class_names[i]+'''.query.filter('''+class_names[i]+'''.'''+id_names[i]+''' == '''+class_names[i].lower()+'''_id).first()
        if not '''+class_names[i].lower()+''':
            return []
        db.session.delete('''+class_names[i].lower()+''')
        db.session.commit()
        return ['''+class_names[i].lower()+'''_id]

    @staticmethod
    def create(new_attrs: '''+class_names[i]+'''Interface) -> '''+class_names[i]+''':
        new_'''+class_names[i].lower()+''' = '''+class_names[i]+'''('''+t[1:-2]+''')
        db.session.add(new_'''+class_names[i].lower()+''')
        db.session.commit()

        return new_'''+class_names[i].lower()+'''

'''
    file.write(temp)