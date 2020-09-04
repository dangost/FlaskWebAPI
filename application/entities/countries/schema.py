from marshmallow import fields, Schema


class CountrySchema(Schema):
    CountryName = fields.String(attribute="CountryName")

    CountryCode = fields.String(attribute="CountryCode")

    NatLangCode = fields.Integer(attribute="NatLangCode")

    CurrencyCode = fields.String(attribute="CurrencyCode")



