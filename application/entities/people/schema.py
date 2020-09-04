from marshmallow import fields, Schema


class PersonSchema(Schema):
    FirstName = fields.String(attribute="FirstName")

    LastName = fields.String(attribute="LastName")

    MiddleName = fields.String(attribute="MiddleName")

    Nickname = fields.String(attribute="Nickname")

    NatLangCode = fields.Integer(attribute="NatLangCode")

    CultureCode = fields.Integer(attribute="CultureCode")

    Gender = fields.String(attribute="Gender")



