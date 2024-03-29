from pytest import fixture

from .interface import InventoryInterface
from .model import Inventory


@fixture
def interface() -> InventoryInterface:
    return InventoryInterface(InventoryId=1, ProductId=1, WarehouseId=1, QuantityOnHand=1, QuantityAvailable=1)


def test_InventoryInterface_create(interface: InventoryInterface):
    assert interface


def test_InventoryInterface_works(interface: InventoryInterface):
    inventory = Inventory(**interface)
    assert inventory
