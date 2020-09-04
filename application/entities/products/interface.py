from mypy_extensions import TypedDict


class ProductInterface(TypedDict, total=False):
    ProductName: str

    Description: str

    Category: int

    WeightClass: str

    WarrantlyPeriod: int

    SupplierId: int

    Status: str

    ListPrice: int

    MinimumPrice: int

    PriceCurrency: str

    CatalogURL: str



