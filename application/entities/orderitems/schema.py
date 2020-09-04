from marshmallow import fields, Schema


class OrderItemSchema(Schema):
    OrderItemId = fields.Integer(attribute="OrderItemId")

    OrderId = fields.Integer(attribute="OrderId")

    ProductId = fields.Integer(attribute="ProductId")

    UnitPrice = fields.Integer(attribute="UnitPrice")

    Quantity = fields.Integer(attribute="Quantity")



