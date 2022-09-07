from pytest import fixture

from .interface import InventoryInterface
from .model import Inventory
from .schema import InventorySchema


@fixture
def schema() -> InventorySchema:
    return InventorySchema()


def test_InventorySchema_create(schema: InventorySchema):
    assert schema


def test_InventorySchema_works(schema: InventorySchema):
    params: InventoryInterface = schema.load(
        {"ProductId": 1, "WarehouseId": 1, "QuantityOnHand": 1, "QuantityAvailable": 1}
    )
    inventory = Inventory(**params)

    assert inventory.ProductId == 1
    assert inventory.WarehouseId == 1
    assert inventory.QuantityOnHand == 1
    assert inventory.QuantityAvailable == 1
