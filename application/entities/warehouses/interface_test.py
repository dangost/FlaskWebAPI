from pytest import fixture

from .interface import WarehouseInterface
from .model import Warehouse


@fixture
def interface() -> WarehouseInterface:
    return WarehouseInterface(WarehouseId=1, LocationId=1, WarehouseName="test")


def test_WarehouseInterface_create(interface: WarehouseInterface):
    assert interface


def test_WarehouseInterface_works(interface: WarehouseInterface):
    warehouse = Warehouse(**interface)
    assert warehouse
