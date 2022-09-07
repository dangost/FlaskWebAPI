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
    folder_path = path + "\\" + list_names[i].lower()

    try:
        os.mkdir(folder_path)
    except BaseException:
        pass
    new_path = folder_path + "\\controller_test.py"
    file = open(new_path, 'w')

    temp = '''from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from .service import ''' + class_names[i] + '''Service
from .schema import ''' + class_names[i] + '''Schema
from .model import ''' + class_names[i] + '''
from .interface import ''' + class_names[i] + '''Interface
from . import BASE_ROUTE


def make_widget(
    id: int = 123, name: str = "Test widget", purpose: str = "Test purpose"
) -> ''' + class_names[i] + ''':
    return Widget(widget_id=id, name=name, purpose=purpose)


class TestWidgetResource:
    @patch.object(
        WidgetService,
        "get_all",
        lambda: [
            make_widget(123, name="Test Widget 1"),
            make_widget(456, name="Test Widget 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                WidgetSchema(many=True)
                .dump(
                    [
                        make_widget(123, name="Test Widget 1"),
                        make_widget(456, name="Test Widget 2"),
                    ]
                )
                
            )
            for r in results:
                assert r in expected

    @patch.object(
        WidgetService, "create", lambda create_request: Widget(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(name="Test widget", purpose="Test purpose")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                WidgetSchema()
                .dump(Widget(name=payload["name"], purpose=payload["purpose"]))
                
            )
            assert result == expected


def fake_update(widget: Widget, changes: WidgetInterface) -> Widget:
    # To fake an update, just return a new object
    updated_Widget = Widget(
        widget_id=widget.widget_id, name=changes["name"], purpose=changes["purpose"]
    )
    return updated_Widget


class TestWidgetIdResource:
    @patch.object(WidgetService, "get_by_id", lambda id: make_widget(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_widget(id=123)
            print(f"result = ", result)
            assert result["widgetId"] == expected.widget_id

    @patch.object(WidgetService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

    @patch.object(WidgetService, "get_by_id", lambda id: make_widget(id=id))
    @patch.object(WidgetService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/123",
                json={"name": "New Widget", "purpose": "New purpose"},
            ).get_json()
            expected = (
                WidgetSchema()
                .dump(Widget(widget_id=123, name="New Widget", purpose="New purpose"))
                
            )
            assert result == expected


'''
    file.write(temp)
