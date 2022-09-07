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

path = r"D:\Projects\Regula\Web\FlaskWebAPI\application\entities"

import os

for i in range(len(class_names)):

    t = ""
    for each in base[i]:
        var = ""
        if base[i].get(each) == "int":
            var = " = Column(Integer())"
        else:
            var = " = Column(String(255))"
        t += "    " + each + var + "\n"

    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path + "\\model.py"
    file = open(new_path, 'w')

    temp = '''from sqlalchemy import Integer, Column, String, ForeignKey
from application import db
from .interface import ''' + class_names[i] + '''Interface


class ''' + class_names[i] + '''(db.Model):

    __tablename__ = "''' + list_names[i] + '''"

''' + t + '''

    def update(self, changes: ''' + class_names[i] + '''Interface):
        for key, val in changes.items():
            setattr(self, key, val)

        return self



'''
    # file.write(temp)
