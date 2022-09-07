from marshmallow import fields, Schema


class PersonLocationSchema(Schema):
    PersonsPersonId = fields.Integer(attribute="PersonsPersonId")

    LocationsLocationsId = fields.Integer(attribute="LocationsLocationsId")

    SubAddress = fields.String(attribute="SubAddress")

    LocationUsage = fields.String(attribute="LocationUsage")

    Notes = fields.String(attribute="Notes")
