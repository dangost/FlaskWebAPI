from marshmallow import fields, Schema


class PhoneNumberSchema(Schema):
    PeoplePersonId = fields.Integer(attribute="PeoplePersonId")

    LocationLocationId = fields.Integer(attribute="LocationLocationId")

    Phonenumber = fields.Integer(attribute="Phonenumber")

    CountryCode = fields.Integer(attribute="CountryCode")

    PhoneType = fields.Integer(attribute="PhoneType")



