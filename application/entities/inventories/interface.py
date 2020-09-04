from mypy_extensions import TypedDict


class InventoryInterface(TypedDict, total=False):
    InventoryId: int

    ProductId: int

    WarehouseId: int

    QuantityOnHand: int

    QuantityAvailable: int



