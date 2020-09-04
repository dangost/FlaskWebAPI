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
        pass
    new_path = folder_path+"\\controller.py"
    file = open(new_path, 'w')

    temp = '''from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import '''+class_names[i]+'''Schema
from .service import '''+list_names[i]+'''Service
from .model import '''+class_names[i]+'''
from .interface import '''+class_names[i]+'''Interface

api = Namespace("'''+class_names[i]+'''", description="Single namespace, single entity")


@api.route("/")
class '''+class_names[i]+'''Resource(Resource):

    @responds(schema='''+class_names[i]+'''Schema(many=True))
    def get(self) -> List['''+class_names[i]+''']:

        return '''+list_names[i]+'''Service.get_all()

    @accepts(schema='''+class_names[i]+'''Schema, api=api)
    @responds(schema='''+class_names[i]+'''Schema)
    def post(self) -> '''+class_names[i]+''':
        obj: dict = request.parsed_obj
        return '''+class_names[i]+'''Service.create(obj)


@api.route("/<int:'''+id_names[i]+'''>")
@api.param("'''+list_names[i]+'''Id", "'''+class_names[i]+''' database ID")
class '''+class_names[i]+'''IdResource(Resource):
    @responds(schema='''+class_names[i]+'''Schema)
    def get(self, '''+id_names[i]+''': int) -> '''+class_names[i]+''':
        return '''+list_names[i]+'''Service.get_by_id('''+id_names[i]+''')

    def delete(self, '''+id_names[i]+''': int) -> Response:
        from flask import jsonify

        id: int = '''+list_names[i]+'''Service.delete_by_id('''+id_names[i]+''')
        return jsonify(dict(status="Success", id=id))

    @accepts(schema='''+class_names[i]+'''Schema, api=api)
    @responds(schema='''+class_names[i]+'''Schema)
    def put(self, '''+id_names[i]+''': int) -> '''+class_names[i]+''':

        changes: '''+class_names[i]+'''Interface = request.parsed_obj
        '''+class_names[i].lower()+''' = '''+list_names[i]+'''Service.get_by_id('''+list_names[i]+''')
        return '''+list_names[i]+'''Service.update('''+class_names[i].lower()+''', changes)

'''
    file.write(temp)