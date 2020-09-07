class_names = ["Country", "Customer", "CustomerCompany", "CustomerEmployee", "Employment", "EmploymentJobs",
               "Inventory", "Location", "OrderItem", "Orders", "Person", "PersonLocation", "PhoneNumber", "Product",
               "RestrictedInfo", "Warehouse"]
list_names = ["Countries", "Customers", "CustomerCompanies", "CustomerEmployees", "Employments", "EmploymentJobs",
              "Inventories", "Locations", "OrderItems", "Orders", "People", "PersonLocations", "PhoneNumbers",
              "Products", "RestrictedInfo", "Warehouses"]
id_names = ["CountryId", "CustomerId", "CompanyId", "CustomerEmployeeId", "EmployeeID", "HRJobId", "InventoryId",
            "LocationId", "OrderItemId", "OrderId", "Id", "PeoplePersonId", "PhoneNumberId", "ProductId", "PersonId",
            "WarehouseId"]
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
    folder_path = path + "\\" + list_names[i].lower()


    t = ""
    b = ""
    q = ""

    for each in base_with_id[i]:
        var = ""
        var1 = ""
        q1 = ""
        if base_with_id[i].get(each) == "int":
            var = ": int = 1"
            var1 = " = 1"
        else:
            var = ":str = \"test\""
            var1 = " = \"test\""
            var5 = "[\"test\"]"
        '''widget_id=1, name="Test widget", purpose="Test purpose"'''
        t += each.lower() + var + ", "
        b += each + "=" + each.lower() + ", "
        q1 += each + var1 + ", "
        '''widget_id=id, name=name, purpose=purpose)'''
        '''widget_id=widget.widget_id, name=changes["name"], purpose=changes["purpose"]'''
    f = id_names[i] + "=" + class_names[i].lower() + "."+id_names[i]+", "
    z = ""
    for each in base[i]:
        var1 = ""
        if base[i].get(each) == "int":
            var1 = "=1"
            var2 = "=payload[1], "

        else:
            var1 = "=\"test\""
            var2 = "=payload[\"test\"], "
        '''widget_id=1, name="Test widget", purpose="Test purpose"'''
        q += each + var1 + ", "
        z += each + var2
        f += each + "=payload[\""+each+"\"], "
        '''widget_id=id, name=name, purpose=purpose)'''
        '''name=payload["name"], purpose=payload["purpose"]'''



    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path + "\\controller_test.py"
    file = open(new_path, 'w')

    temp = '''from unittest.mock import patch
from flask.testing import FlaskClient
from .service import ''' + list_names[i] + '''Service
from .schema import ''' + class_names[i] + '''Schema
from .model import ''' + class_names[i] + '''
from . import BASE_ROUTE


def make_'''+class_names[i].lower()+'''(
    '''+t[0:-2]+'''
) -> ''' + class_names[i] + ''':
    return '''+class_names[i]+'''('''+b[0:-2]+''')


class Test''' + class_names[i] + '''Resource:
    @patch.object(
        ''' + list_names[i] + '''Service,
        "get_all",
        lambda: [
            make_''' + class_names[i].lower() + '''(),
            make_'''+class_names[i].lower()+'''('''+id_names[i]+'''=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                ''' + class_names[i] + '''Schema(many=True)
                .dump(
                    [
                        make_''' + class_names[i].lower() + '''(),
                        make_'''+class_names[i].lower()+'''('''+id_names[i]+'''=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        ''' + list_names[i] + '''Service, "create", lambda create_request: ''' + class_names[i] + '''(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict('''+q[0:-2]+''')
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                ''' + class_names[i] + '''Schema()
                .dump(''' + class_names[i] + '''('''+z[0:-2]+'''))

            )
            assert result == expected


class Test''' + class_names[i] + '''IdResource:
    @patch.object(''' + list_names[i] + '''Service, "get_by_id", lambda id: make_''' + class_names[i].lower() + '''(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_''' + class_names[i].lower() + '''(id=123)
            print(f"result = ", result)
            assert result["''' + id_names[i] + '''"] == expected.''' + id_names[i] + '''

    @patch.object(''' + list_names[i] + '''Service, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

'''
    file.write(temp)