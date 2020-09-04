from marshmallow import fields, Schema


class InventorySchema(Schema):
    ProductId = fields.Integer(attribute="ProductId")

    WarehouseId = fields.Integer(attribute="WarehouseId")

    QuantityOnHand = fields.Integer(attribute="QuantityOnHand")

    QuantityAvailable = fields.Integer(attribute="QuantityAvailable")



