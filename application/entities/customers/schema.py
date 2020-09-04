from marshmallow import fields, Schema


class CustomerSchema(Schema):
    PersonId = fields.Integer(attribute="PersonId")

    CustomEmployeeId = fields.Integer(attribute="CustomEmployeeId")

    AccountMgrId = fields.Integer(attribute="AccountMgrId")

    IncomeLevel = fields.Integer(attribute="IncomeLevel")



