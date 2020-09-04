from mypy_extensions import TypedDict


class WarehouseInterface(TypedDict, total=False):
    LocationId: int

    WarehouseName: str



