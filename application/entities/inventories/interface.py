from mypy_extensions import TypedDict


class InventoryInterface(TypedDict, total=False):
    ProductId: int

    WarehouseId: int

    QuantityOnHand: int

    QuantityAvaileble: int



