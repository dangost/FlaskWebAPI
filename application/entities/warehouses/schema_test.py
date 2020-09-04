from pytest import fixture

from .model import Warehouse
from .schema import WarehouseSchema
from .interface import WarehouseInterface


@fixture
def schema() -> WarehouseSchema:
    return WarehouseSchema()


def test_WarehouseSchema_create(schema: WarehouseSchema):
    assert schema


def test_WarehouseSchema_works(schema: WarehouseSchema):
    params: WarehouseInterface = schema.load(
        {"WarehouseId": 1, "LocationId": 1, "WarehouseName": "test"}
    )
    warehouse = Warehouse(**params)

    assert warehouse.WarehouseId == 1
    assert warehouse.LocationId == 1
    assert warehouse.WarehouseName == "test"


