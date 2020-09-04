from marshmallow import fields, Schema


class WarehouseSchema(Schema):
    LocationId = fields.Integer(attribute="LocationId")

    WarehouseName = fields.String(attribute="WarehouseName")



