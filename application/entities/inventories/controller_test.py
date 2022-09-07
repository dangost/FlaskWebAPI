from flask.testing import FlaskClient
from unittest.mock import patch

from . import BASE_ROUTE
from .model import Inventory
from .schema import InventorySchema
from .service import InventoriesService


def make_inventory(
        inventoryid: int = 1, productid: int = 1, warehouseid: int = 1, quantityonhand: int = 1,
        quantityavailable: int = 1
) -> Inventory:
    return Inventory(InventoryId=inventoryid, ProductId=productid, WarehouseId=warehouseid,
                     QuantityOnHand=quantityonhand, QuantityAvailable=quantityavailable)


class TestInventoryResource:
    @patch.object(
        InventoriesService,
        "get_all",
        lambda: [
            make_inventory(),
            make_inventory(InventoryId=20),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                InventorySchema(many=True)
                    .dump(
                    [
                        make_inventory(),
                        make_inventory(InventoryId=20),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        InventoriesService, "create", lambda create_request: Inventory(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(ProductId=1, WarehouseId=1, QuantityOnHand=1, QuantityAvailable=1)
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                InventorySchema()
                    .dump(Inventory(ProductId=payload[1], WarehouseId=payload[1], QuantityOnHand=payload[1],
                                    QuantityAvailable=payload[1]))

            )
            assert result == expected


class TestInventoryIdResource:
    @patch.object(InventoriesService, "get_by_id", lambda id: make_inventory(id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected = make_inventory(id=123)
            print(f"result = ", result)
            assert result["InventoryId"] == expected.InventoryId

    @patch.object(InventoriesService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id=123)
            assert result == expected
