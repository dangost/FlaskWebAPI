from marshmallow import fields, Schema


class LocationSchema(Schema):
    CountryId = fields.Integer(attribute="CountryId")

    AdressLine1 = fields.String(attribute="AdressLine1")

    AdressLine2 = fields.String(attribute="AdressLine2")

    City = fields.String(attribute="City")

    State = fields.String(attribute="State")

    District = fields.String(attribute="District")

    PostalCode = fields.String(attribute="PostalCode")

    LocationTypeCode = fields.Integer(attribute="LocationTypeCode")

    Description = fields.String(attribute="Description")

    ShippingNotes = fields.String(attribute="ShippingNotes")

    CountriesCountryId = fields.Integer(attribute="CountriesCountryId")



