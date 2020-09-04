from marshmallow import fields, Schema


class OrderItemSchema(Schema):
    OrderId = fields.Integer(attribute="OrderId")

    ProductId = fields.Integer(attribute="ProductId")

    UnitPrice = fields.Integer(attribute="UnitPrice")

    Quantity = fields.Integer(attribute="Quantity")



