from unittest.mock import patch
from flask.testing import FlaskClient
from .service import WarehousesService
from .schema import WarehouseSchema
from .model import Warehouse
from . import BASE_ROUTE


def make_warehouse(
    warehouseid: int = 1, locationid: int = 1, warehousename:str = "test"
) -> Warehouse:
    return Warehouse(WarehouseId=warehouseid, LocationId=locationid, WarehouseName=warehousename)


class TestWarehouseResource:
    @patch.object(
        WarehousesService,
        "get_all",
        lambda: [
            make_warehouse(),
            make_warehouse(WarehouseId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                WarehouseSchema(many=True)
                .dump(
                    [
                        make_warehouse(),
                        make_warehouse(WarehouseId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        WarehousesService, "create", lambda create_request: Warehouse(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:

            payload = dict(WarehouseId=1, LocationId=1, WarehouseName="test")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                WarehouseSchema()
                .dump(Warehouse(WarehouseId=payload[1], LocationId=payload[1], WarehouseName=payload["test"]))

            )
            assert result == expected


class TestWarehouseIdResource:
    @patch.object(WarehousesService, "get_by_id", lambda id: make_warehouse(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_warehouse(id=123)
            print(f"result = ", result)
            assert result["WarehouseId"] == expected.WarehouseId

    @patch.object(WarehousesService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected

