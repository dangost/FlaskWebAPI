from marshmallow import fields, Schema


class PhoneNumberSchema(Schema):
    PhoneNumberId = fields.Integer(attribute="PhoneNumberId")

    PeoplePersonId = fields.Integer(attribute="PeoplePersonId")

    LocationLocationId = fields.Integer(attribute="LocationLocationId")

    PhoneNumber = fields.Integer(attribute="PhoneNumber")

    CountryCode = fields.Integer(attribute="CountryCode")

    PhoneType = fields.Integer(attribute="PhoneType")



