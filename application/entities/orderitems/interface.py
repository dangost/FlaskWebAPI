from mypy_extensions import TypedDict


class OrderItemInterface(TypedDict, total=False):
    OrderItemId: int

    OrderId: int

    ProductId: int

    UnitPrice: int

    Quantity: int



