from marshmallow import fields, Schema


class PersonLocationSchema(Schema):
    PeoplePersonId = fields.Integer(attribute="PeoplePersonId")

    LocationsLocationsId = fields.Integer(attribute="LocationsLocationsId")

    SubAddress = fields.String(attribute="SubAddress")

    LocationUsage = fields.String(attribute="LocationUsage")

    Notes = fields.String(attribute="Notes")



