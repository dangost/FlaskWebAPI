from mypy_extensions import TypedDict


class OrdersInterface(TypedDict, total=False):
    OrderId: int

    CustomerId: int

    SalesRepId: int

    OrderDate: str

    OrderCode: str

    OrderStatus: str

    OrderTotal: int

    OrderCurrency: str

    PromotionCode: str
