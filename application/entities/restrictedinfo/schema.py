from marshmallow import fields, Schema


class RestrictedInfoSchema(Schema):
    PersonId = fields.Integer(attribute="PersonId")

    DateOfBirth = fields.String(attribute="DateOfBirth")

    DateOfDeath = fields.String(attribute="DateOfDeath")

    GovernmentId = fields.String(attribute="GovernmentId")

    PassportId = fields.String(attribute="PassportId")

    HireDire = fields.String(attribute="HireDire")

    SeniorityCode = fields.Integer(attribute="SeniorityCode")



