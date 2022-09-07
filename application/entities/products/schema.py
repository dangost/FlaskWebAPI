from marshmallow import fields, Schema


class ProductSchema(Schema):
    ProductId = fields.Integer(attribute="ProductId")

    ProductName = fields.String(attribute="ProductName")

    Description = fields.String(attribute="Description")

    Category = fields.Integer(attribute="Category")

    WeightClass = fields.String(attribute="WeightClass")

    WarrantyPeriod = fields.Integer(attribute="WarrantyPeriod")

    SupplierId = fields.Integer(attribute="SupplierId")

    Status = fields.String(attribute="Status")

    ListPrice = fields.Integer(attribute="ListPrice")

    MinimumPrice = fields.Integer(attribute="MinimumPrice")

    PriceCurrency = fields.String(attribute="PriceCurrency")

    CatalogURL = fields.String(attribute="CatalogURL")
