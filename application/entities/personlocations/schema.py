from marshmallow import fields, Schema


class PersonLocationSchema(Schema):
    LocationsLocationsId = fields.Integer(attribute="LocationsLocationsId")

    SubAdress = fields.String(attribute="SubAdress")

    LocationUsage = fields.String(attribute="LocationUsage")

    Notes = fields.String(attribute="Notes")



