from mypy_extensions import TypedDict


class OrderItemInterface(TypedDict, total=False):
    OrderId: int

    ProductId: int

    UnitPrice: int

    Quantity: int



