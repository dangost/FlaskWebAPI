from pytest import fixture
from .model import Warehouse
from .interface import WarehouseInterface


@fixture
def interface() -> WarehouseInterface:
    return WarehouseInterface(WarehouseId=1, LocationId=1, WarehouseName="test")


def test_WarehouseInterface_create(interface: WarehouseInterface):
    assert interface


def test_WarehouseInterface_works(interface: WarehouseInterface):
    warehouse = Warehouse(**interface)
    assert warehouse

