from marshmallow import fields, Schema


class OrdersSchema(Schema):
    OrderId = fields.Integer(attribute="OrderId")

    CustomerId = fields.Integer(attribute="CustomerId")

    SalesRepId = fields.Integer(attribute="SalesRepId")

    OrderDate = fields.String(attribute="OrderDate")

    OrderCode = fields.String(attribute="OrderCode")

    OrderStatus = fields.String(attribute="OrderStatus")

    OrderTotal = fields.Integer(attribute="OrderTotal")

    OrderCurrency = fields.String(attribute="OrderCurrency")

    PromotionCode = fields.String(attribute="PromotionCode")



