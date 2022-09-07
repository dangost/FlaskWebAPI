from mypy_extensions import TypedDict


class WarehouseInterface(TypedDict, total=False):
    WarehouseId: int

    LocationId: int

    WarehouseName: str
