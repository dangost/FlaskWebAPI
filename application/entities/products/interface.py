from mypy_extensions import TypedDict


class ProductInterface(TypedDict, total=False):
    ProductId: int

    ProductName: str

    Description: str

    Category: int

    WeightClass: str

    WarrantyPeriod: int

    SupplierId: int

    Status: str

    ListPrice: int

    MinimumPrice: int

    PriceCurrency: str

    CatalogURL: str



