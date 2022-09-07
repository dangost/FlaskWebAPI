from marshmallow import fields, Schema


class WarehouseSchema(Schema):
    WarehouseId = fields.Integer(attribute="WarehouseId")

    LocationId = fields.Integer(attribute="LocationId")

    WarehouseName = fields.String(attribute="WarehouseName")
